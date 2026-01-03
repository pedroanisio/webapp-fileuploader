# ClipDrop

ClipDrop is a Flask web app for authenticated file uploads and shared clipboard entries.
Upload files, save clipboard text or images, and share/download them from a single UI. Files can be
encrypted at rest and are cleaned up automatically every 24 hours.

## Features

- Drag-and-drop file uploads with download/delete actions
- Clipboard text and image capture with a dedicated viewer
- Favorites, tags, and folder organization for clipboard items
- Per-item retention control (keep beyond 24 hours)
- GitHub OAuth sign-in (required to access the app)
- AES-256-GCM encryption for files at rest (optional)
- Automatic cleanup of files after 24 hours
- Pluggable storage backends (local filesystem or S3-compatible)
- Production-ready for Digital Ocean App Platform

## Supported File Types

`txt`, `pdf`, `png`, `jpg`, `jpeg`, `gif`, `pst`, `md`, `json`, `zip`, `tar`, `py`, `html`, `css`

## Technology Stack

- Flask, Flask-Login, Flask-Dance
- Flask-SQLAlchemy + SQLite/PostgreSQL
- APScheduler
- boto3 (S3/Spaces storage)
- Bootstrap + JavaScript

## Setup and Installation

### Prerequisites

- Python 3.12+
- uv or pip

### Environment Variables

Copy `.env.example` to `.env` and configure:

```sh
cp .env.example .env
```

**Required variables:**
```
SECRET_KEY=your-unique-secret
GITHUB_OAUTH_CLIENT_ID=your-client-id
GITHUB_OAUTH_CLIENT_SECRET=your-secret
```

**Optional variables:**
```
ENCRYPTION_KEY=your-base64-encoded-key   # AES-256 encryption (recommended)
DATABASE_URL=sqlite:///clipdrop.db       # or postgresql://...
PORT=3000
```

**Storage configuration:**
```
STORAGE_TYPE=local                        # "local" or "s3"
UPLOAD_FOLDER=uploads                     # for local storage

# For S3/Spaces storage:
SPACES_BUCKET=your-bucket-name
SPACES_ENDPOINT=https://nyc3.digitaloceanspaces.com
SPACES_REGION=nyc3
SPACES_ACCESS_KEY=your-access-key
SPACES_SECRET_KEY=your-secret-key
SPACES_PREFIX=uploads
```

Generate secrets with:
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

Build and run the container:
```sh
docker build -t clipdrop .
docker run -p 3000:3000 --env-file .env clipdrop
```

### Usage

- Open `http://localhost:3000`.
- Sign in with GitHub OAuth.
- Upload files via drag-and-drop or save clipboard text/images.
- View, download, or delete uploaded items.
- Favorite, tag, rename, and move clipboard items into folders.

### File Structure

```
clipdrop/
├── src/clipdrop/
│   ├── __init__.py
│   ├── __main__.py
│   ├── app.py
│   ├── crypto.py
│   ├── extensions.py
│   ├── helpers.py
│   ├── models.py
│   ├── storage.py
│   ├── static/
│   │   ├── styles.css
│   │   └── js/
│   │       ├── clipboard.js
│   │       ├── files.js
│   │       ├── modal.js
│   │       ├── navigation.js
│   │       ├── theme.js
│   │       └── toast.js
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── clipboard_view.html
│       ├── clipboard_edit.html
│       ├── shared_clipboard.html
│       ├── macros.html
│       └── components/
│           ├── bottom_nav.html
│           ├── modal.html
│           ├── navigation.html
│           └── toast.html
├── tests/
├── scripts/
├── pyproject.toml
└── Dockerfile
```

## Deployment

### Dokploy + Digital Ocean Spaces

The application is deployed using [Dokploy](https://dokploy.com/) with Digital Ocean Spaces for file storage.

**Prerequisites:**
1. Create a Digital Ocean Space for file storage
2. Generate Spaces access keys (API > Spaces Keys)
3. Register a GitHub OAuth app with callback URL: `https://clipdrop.is42.io/login/github/authorized`

**Environment variables:**
```
SECRET_KEY=your-secret-key
GITHUB_OAUTH_CLIENT_ID=your-client-id
GITHUB_OAUTH_CLIENT_SECRET=your-client-secret
DATABASE_URL=postgresql://user:pass@host:5432/clipdrop
STORAGE_TYPE=s3
SPACES_BUCKET=your-bucket
SPACES_ENDPOINT=https://nyc3.digitaloceanspaces.com
SPACES_REGION=nyc3
SPACES_ACCESS_KEY=your-access-key
SPACES_SECRET_KEY=your-secret-key
```

**Dokploy setup:**
1. Create a new application in Dokploy
2. Connect your GitHub repository
3. Configure environment variables in the Dokploy dashboard
4. Set the exposed port to `3000`
5. Deploy

The Dockerfile uses Gunicorn with 4 workers on port 3000.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

### License

This project is licensed under the MIT License.

### Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [APScheduler](https://apscheduler.readthedocs.io/)
- [Bootstrap](https://getbootstrap.com/)
