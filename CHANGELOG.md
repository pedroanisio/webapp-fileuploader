# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-02

### Added

- Initial release with src-layout structure
- File upload functionality with drag-and-drop support
- Clipboard sharing feature for text and images
- AES-256-GCM encryption for data at rest
- Automatic file cleanup after 24 hours
- Docker support with docker-compose
- Comprehensive test suite (unit and integration tests)
- Modern `pyproject.toml` configuration (PEP 621)

### Changed

- Migrated from flat layout to src-layout structure
- Replaced `requirements.txt` with `pyproject.toml`
- Refactored app.py to use Flask application factory pattern

### Security

- Added AES-256-GCM encryption for uploaded files
- Secure filename handling with Werkzeug
- Environment-based secret key management
