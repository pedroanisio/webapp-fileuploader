from flask import Flask, request, redirect, url_for, render_template, send_file, flash, jsonify
from werkzeug.utils import secure_filename
import os
import uuid
from datetime import datetime, timedelta
from io import BytesIO
from apscheduler.schedulers.background import BackgroundScheduler
import logging
from dotenv import load_dotenv
from crypto import encrypt_data, safe_decrypt, load_key_from_env

# Load environment variables
load_dotenv()

UPLOAD_FOLDER = 'uploads'
CLIPBOARD_FOLDER = 'clipboard'
ALLOWED_EXTENSIONS = {
    'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'pst',
    'md', 'json', 'zip', 'tar', 'py', 'html', 'css',
}
SECRET_KEY = os.getenv('SECRET_KEY')
ENCRYPTION_KEY_B64 = os.getenv('ENCRYPTION_KEY')

if not SECRET_KEY:
    raise RuntimeError(
        'SECRET_KEY is not set. Run ./generate_secret.sh to create a .env file '
        'or export SECRET_KEY in the environment.'
    )

# Load encryption key (optional for backward compatibility)
ENCRYPTION_KEY = None
if ENCRYPTION_KEY_B64:
    try:
        ENCRYPTION_KEY = load_key_from_env(ENCRYPTION_KEY_B64)
        logging.info('Encryption key loaded successfully')
    except Exception as e:
        logging.warning(f'Failed to load encryption key: {e}. Files will not be encrypted.')
else:
    logging.warning('ENCRYPTION_KEY not set. Files will be stored unencrypted.')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CLIPBOARD_FOLDER'] = CLIPBOARD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 * 1024  # 10GB
app.config['SECRET_KEY'] = SECRET_KEY  # Load SECRET_KEY from environment

# Ensure the upload and clipboard folders exist
for folder in [UPLOAD_FOLDER, CLIPBOARD_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Configure logging
logging.basicConfig(level=logging.INFO)

def wants_json_response():
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

def respond_upload(message, category, status, redirect_url):
    if wants_json_response():
        payload = {
            'status': 'success' if status < 400 else 'error',
            'message': message
        }
        return jsonify(payload), status
    flash(message, category)
    return redirect(redirect_url)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def human_readable_size(size_bytes):
    """Convert bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"

def get_file_extension(filename):
    """Get file extension from filename."""
    if '.' in filename:
        return filename.rsplit('.', 1)[1].lower()
    return ''


def save_file_encrypted(data: bytes, file_path: str) -> None:
    """Save file with encryption if key is available."""
    if ENCRYPTION_KEY:
        data = encrypt_data(data, ENCRYPTION_KEY)
    with open(file_path, 'wb') as f:
        f.write(data)


def read_file_decrypted(file_path: str) -> bytes:
    """Read file and decrypt if encrypted."""
    with open(file_path, 'rb') as f:
        data = f.read()
    if ENCRYPTION_KEY:
        data, _ = safe_decrypt(data, ENCRYPTION_KEY)
    return data


def get_file_properties(filename, folder):
    file_path = os.path.join(folder, filename)
    file_size = os.path.getsize(file_path)
    file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
    content = ''
    if filename.endswith('.txt'):
        try:
            data = read_file_decrypted(file_path)
            content = data.decode('utf-8')
        except (IOError, UnicodeDecodeError):
            content = '[Unable to read file content]'
    return {
        'name': filename,
        'size': file_size,
        'size_human': human_readable_size(file_size),
        'creation_time': file_creation_time,
        'content': content,
        'extension': get_file_extension(filename)
    }

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            logging.error('No file part')
            return respond_upload(
                'No file selected. Please choose a file to upload.',
                'warning',
                400,
                request.url
            )
        file = request.files['file']
        if file.filename == '':
            logging.error('No selected file')
            return respond_upload(
                'No file selected. Please choose a file to upload.',
                'warning',
                400,
                request.url
            )
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = f"{uuid.uuid4()}_{filename}"
            try:
                file_data = file.read()
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                save_file_encrypted(file_data, file_path)
                logging.info(f'File {filename} successfully uploaded (encrypted: {ENCRYPTION_KEY is not None})')
                return respond_upload(
                    'File successfully uploaded.',
                    'success',
                    200,
                    url_for('upload_file')
                )
            except Exception as e:
                logging.error(f'File upload failed: {e}')
                return respond_upload(
                    'Upload failed. Please try again.',
                    'danger',
                    500,
                    request.url
                )
        else:
            logging.warning('File type not allowed')
            return respond_upload(
                'File type not allowed. Please choose a supported file.',
                'warning',
                400,
                request.url
            )
    files = [get_file_properties(file, app.config['UPLOAD_FOLDER']) for file in os.listdir(app.config['UPLOAD_FOLDER'])]
    clipboard_files = [get_file_properties(file, app.config['CLIPBOARD_FOLDER']) for file in os.listdir(app.config['CLIPBOARD_FOLDER'])]
    return render_template('index.html', files=files, clipboard_files=clipboard_files, allowed_extensions=ALLOWED_EXTENSIONS)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded file, decrypting if necessary."""
    filename = secure_filename(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(file_path):
        return jsonify({'status': 'error', 'message': 'File not found'}), 404

    try:
        data = read_file_decrypted(file_path)
        # Determine mimetype from extension
        ext = get_file_extension(filename)
        mimetype_map = {
            'txt': 'text/plain',
            'pdf': 'application/pdf',
            'png': 'image/png',
            'jpg': 'image/jpeg',
            'jpeg': 'image/jpeg',
            'gif': 'image/gif',
            'json': 'application/json',
            'html': 'text/html',
            'css': 'text/css',
            'md': 'text/markdown',
            'py': 'text/x-python',
            'zip': 'application/zip',
            'tar': 'application/x-tar',
        }
        mimetype = mimetype_map.get(ext, 'application/octet-stream')
        return send_file(BytesIO(data), mimetype=mimetype, download_name=filename)
    except Exception as e:
        logging.error(f'Failed to serve file {filename}: {e}')
        return jsonify({'status': 'error', 'message': 'Failed to read file'}), 500

@app.route('/clipboard/<filename>')
def clipboard_file(filename):
    """View clipboard content in a nice template."""
    file_path = os.path.join(app.config['CLIPBOARD_FOLDER'], filename)
    if not os.path.exists(file_path):
        return render_template('clipboard_view.html', file=None, is_text=False)

    file_props = get_file_properties(filename, app.config['CLIPBOARD_FOLDER'])
    is_text = filename.endswith(('.txt', '.md', '.json', '.py', '.html', '.css'))

    return render_template('clipboard_view.html', file=file_props, is_text=is_text)

@app.route('/clipboard/raw/<filename>')
def clipboard_file_raw(filename):
    """Serve raw clipboard file for download, decrypting if necessary."""
    filename = secure_filename(filename)
    file_path = os.path.join(app.config['CLIPBOARD_FOLDER'], filename)
    if not os.path.exists(file_path):
        return jsonify({'status': 'error', 'message': 'File not found'}), 404

    try:
        data = read_file_decrypted(file_path)
        ext = get_file_extension(filename)
        mimetype_map = {
            'txt': 'text/plain',
            'png': 'image/png',
            'jpg': 'image/jpeg',
            'jpeg': 'image/jpeg',
            'gif': 'image/gif',
            'md': 'text/markdown',
            'json': 'application/json',
        }
        mimetype = mimetype_map.get(ext, 'application/octet-stream')
        return send_file(BytesIO(data), mimetype=mimetype, download_name=filename)
    except Exception as e:
        logging.error(f'Failed to serve clipboard file {filename}: {e}')
        return jsonify({'status': 'error', 'message': 'Failed to read file'}), 500

@app.route('/shared-clipboard')
def shared_clipboard():
    clipboard_files = [get_file_properties(file, app.config['CLIPBOARD_FOLDER']) for file in os.listdir(app.config['CLIPBOARD_FOLDER'])]
    clipboard_files.sort(key=lambda x: x['creation_time'], reverse=True)
    return render_template('shared_clipboard.html', clipboard_files=clipboard_files)

@app.route('/clipboard', methods=['POST'])
def clipboard():
    data = request.form['clipboard_data']
    if 'image' in request.files:
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = f"clipboard_{uuid.uuid4()}_{secure_filename(file.filename)}"
            file_data = file.read()
            file_path = os.path.join(app.config['CLIPBOARD_FOLDER'], filename)
            save_file_encrypted(file_data, file_path)
            return jsonify({'status': 'success', 'message': 'Image saved', 'filename': filename})
    else:
        filename = f"clipboard_{uuid.uuid4()}.txt"
        file_path = os.path.join(app.config['CLIPBOARD_FOLDER'], filename)
        save_file_encrypted(data.encode('utf-8'), file_path)
        return jsonify({'status': 'success', 'message': 'Text saved', 'filename': filename})

@app.route('/delete/<path:filename>', methods=['DELETE'])
def delete_file(filename):
    filename = secure_filename(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            logging.info(f'File {filename} deleted by user')
            return jsonify({'status': 'success', 'message': 'File deleted'})
        except Exception as e:
            logging.error(f'Failed to delete file {filename}: {e}')
            return jsonify({'status': 'error', 'message': 'Failed to delete file'}), 500
    return jsonify({'status': 'error', 'message': 'File not found'}), 404

@app.route('/delete/clipboard/<path:filename>', methods=['DELETE'])
def delete_clipboard_file(filename):
    filename = secure_filename(filename)
    file_path = os.path.join(app.config['CLIPBOARD_FOLDER'], filename)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            logging.info(f'Clipboard file {filename} deleted by user')
            return jsonify({'status': 'success', 'message': 'Clipboard item deleted'})
        except Exception as e:
            logging.error(f'Failed to delete clipboard file {filename}: {e}')
            return jsonify({'status': 'error', 'message': 'Failed to delete clipboard item'}), 500
    return jsonify({'status': 'error', 'message': 'Clipboard item not found'}), 404

def cleanup_files():
    now = datetime.now()
    for folder in [UPLOAD_FOLDER, CLIPBOARD_FOLDER]:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
            if now - file_creation_time > timedelta(days=1):
                os.remove(file_path)
                logging.info(f'Removed file {filename}')

# Setup and start the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=cleanup_files, trigger="interval", hours=24)
scheduler.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3010, debug=True)
