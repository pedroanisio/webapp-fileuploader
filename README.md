# ClipDrop

ClipDrop is a Flask web app for authenticated file uploads and shared clipboard entries.
Upload files, save clipboard text or images, and share/download them from a single UI. Files can be
encrypted at rest and are cleaned up automatically every 24 hours.

## Features

- Drag-and-drop file uploads with download/delete actions
- Clipboard text and image capture with a dedicated viewer
- GitHub OAuth sign-in (required to access the app)
- AES-256-GCM encryption for files at rest (optional)
- Automatic cleanup of files after 24 hours
- Local SQLite storage for user accounts and OAuth tokens

## Supported File Types

`txt`, `pdf`, `png`, `jpg`, `jpeg`, `gif`, `pst`, `md`, `json`, `zip`, `tar`, `py`, `html`, `css`

## Technology Stack

- Flask, Flask-Login, Flask-Dance
- Flask-SQLAlchemy + SQLite (default)
- APScheduler
- Bootstrap + JavaScript

## Setup and Installation

### Prerequisites

- Python 3.10+
- uv or pip

### Environment Variables

Create a `.env` file in the project root directory (required for local/dev and Docker):

```
SECRET_KEY=your-unique-secret
ENCRYPTION_KEY=your-base64-encoded-key
GITHUB_OAUTH_CLIENT_ID=your-client-id
GITHUB_OAUTH_CLIENT_SECRET=your-secret
DATABASE_URL=sqlite:///clipdrop.db
UPLOAD_FOLDER=uploads
CLIPBOARD_FOLDER=clipboard
PORT=3000
```

- `SECRET_KEY` is required to boot the app.
- `ENCRYPTION_KEY` is optional; when unset, files are stored unencrypted.
- GitHub OAuth credentials are required to sign in.
- `DATABASE_URL`, `UPLOAD_FOLDER`, `CLIPBOARD_FOLDER`, and `PORT` are optional overrides.

Generate a `.env` with `SECRET_KEY` + `ENCRYPTION_KEY`:
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

3. **Run the application (default http://localhost:3000):**
   ```sh
   clipdrop
   # or
   python -m clipdrop
   ```

### Docker

Use the production compose file (runs gunicorn on port 3000, mapped to 3020 locally):
```sh
docker compose up --build
```

For development with the Flask server:
```sh
docker compose -f docker-compose.dev.yml up --build
```

### Usage

- Open `http://localhost:3000` (or `http://localhost:3020` when using Docker).
- Sign in with GitHub OAuth.
- Upload files via drag-and-drop or save clipboard text/images.
- View, download, or delete uploaded items.

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
