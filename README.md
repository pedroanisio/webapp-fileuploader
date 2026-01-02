# ClipDrop

ClipDrop is a web application that allows users to upload files and manage clipboard content. Users can drag and drop files for upload, view and download uploaded files, and manage clipboard text and images. Clipboard text content can be viewed in an accordion-style interface, and users can easily copy text content with a click.

## Features

- Drag and drop file upload
- View and download uploaded files
- Clipboard text and image management
- View text content in an accordion-style interface
- Copy text content with a click
- Files are automatically cleaned up every 24 hours
- AES-256-GCM encryption for files at rest
- GitHub OAuth authentication

## Technology Stack

- Flask (Python web framework)
- Flask-SQLAlchemy (Database ORM)
- Flask-Login & Flask-Dance (Authentication)
- APScheduler (Python library for scheduling tasks)
- Bootstrap (CSS framework for responsive design)
- JavaScript for client-side functionality

## Setup and Installation

### Prerequisites

- Docker
- Python 3.10+
- uv or pip

### Environment Variables

Create a `.env` file in the project root directory with the following content:
```
SECRET_KEY=your-unique-secret
ENCRYPTION_KEY=your-base64-encoded-key  # Optional
GITHUB_OAUTH_CLIENT_ID=your-client-id    # Optional
GITHUB_OAUTH_CLIENT_SECRET=your-secret   # Optional
```

You can generate a secret key automatically:
```sh
./scripts/generate_secret.sh
```


### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/pedroanisio/clipdrop.git
    cd clipdrop
    ```

2. **Install dependencies:**
    ```sh
    pip install .
    # or with uv
    uv pip install .
    ```

3. **Run the application:**
    ```sh
    clipdrop
    # or
    python -m clipdrop
    ```

### Docker

1. **Build and run the Docker container:**
    ```sh
    docker build -t clipdrop .
    docker run -p 3010:3010 clipdrop
    ```

   Or use `docker-compose`:
    ```sh
    docker-compose up
    ```

### Usage

- Open your web browser and navigate to `http://localhost:3010`.
- Sign in with GitHub (if OAuth is configured) or access directly.
- Drag and drop files into the designated area to upload.
- View, download, and manage uploaded files.
- Paste text into the clipboard section and save it. View, download, and copy clipboard text content.

### File Structure

```
clipdrop/
├── src/clipdrop/
│   ├── __init__.py
│   ├── __main__.py
│   ├── app.py
│   ├── crypto.py
│   ├── extensions.py
│   ├── models.py
│   ├── static/
│   │   └── styles.css
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── clipboard_view.html
│       └── shared_clipboard.html
├── tests/
├── docs/
├── scripts/
├── pyproject.toml
├── Dockerfile
└── docker-compose.yaml
```

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

### License

This project is licensed under the MIT License.

### Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [APScheduler](https://apscheduler.readthedocs.io/)
- [Bootstrap](https://getbootstrap.com/)
