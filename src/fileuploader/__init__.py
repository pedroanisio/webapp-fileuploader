"""
File Uploader & Clipboard Manager

A Flask-based web application for secure file uploads and clipboard sharing.
"""

__version__ = "1.0.0"
__author__ = "File Uploader Team"

from fileuploader.app import create_app

__all__ = ["create_app", "__version__"]
