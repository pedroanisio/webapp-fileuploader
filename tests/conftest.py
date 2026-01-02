"""Pytest configuration and fixtures."""

import os
import tempfile

import pytest

from clipdrop.app import create_app


@pytest.fixture
def app():
    """Create application for testing."""
    # Create temporary directories for uploads and clipboard
    with tempfile.TemporaryDirectory() as tmpdir:
        upload_folder = os.path.join(tmpdir, "uploads")
        clipboard_folder = os.path.join(tmpdir, "clipboard")
        os.makedirs(upload_folder)
        os.makedirs(clipboard_folder)

        # Set environment variables for testing
        os.environ["SECRET_KEY"] = "test-secret-key-for-testing"

        app = create_app(
            config={
                "TESTING": True,
                "UPLOAD_FOLDER": upload_folder,
                "CLIPBOARD_FOLDER": clipboard_folder,
            }
        )

        yield app


@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create test CLI runner."""
    return app.test_cli_runner()
