"""Integration tests for Flask routes."""

import io


class TestIndexRoute:
    """Tests for the index/upload route."""

    def test_index_returns_200(self, client):
        """Index page should return 200."""
        response = client.get("/")
        assert response.status_code == 200

    def test_index_contains_upload_form(self, client):
        """Index page should contain upload form elements."""
        response = client.get("/")
        assert b"upload" in response.data.lower()


class TestFileUpload:
    """Tests for file upload functionality."""

    def test_upload_valid_file(self, client):
        """Should successfully upload a valid file."""
        data = {"file": (io.BytesIO(b"test content"), "test.txt")}
        response = client.post(
            "/",
            data=data,
            content_type="multipart/form-data",
            follow_redirects=True,
        )
        assert response.status_code == 200

    def test_upload_no_file(self, client):
        """Should handle missing file gracefully."""
        response = client.post(
            "/",
            data={},
            content_type="multipart/form-data",
            headers={"X-Requested-With": "XMLHttpRequest"},
        )
        assert response.status_code == 400

    def test_upload_empty_filename(self, client):
        """Should reject empty filename."""
        data = {"file": (io.BytesIO(b""), "")}
        response = client.post(
            "/",
            data=data,
            content_type="multipart/form-data",
            headers={"X-Requested-With": "XMLHttpRequest"},
        )
        assert response.status_code == 400

    def test_upload_disallowed_extension(self, client):
        """Should reject files with disallowed extensions."""
        data = {"file": (io.BytesIO(b"malicious"), "virus.exe")}
        response = client.post(
            "/",
            data=data,
            content_type="multipart/form-data",
            headers={"X-Requested-With": "XMLHttpRequest"},
        )
        assert response.status_code == 400


class TestClipboard:
    """Tests for clipboard functionality."""

    def test_clipboard_post_text(self, client):
        """Should save text to clipboard."""
        response = client.post(
            "/clipboard",
            data={"clipboard_data": "Test clipboard content"},
        )
        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data["status"] == "success"

    def test_shared_clipboard_returns_200(self, client):
        """Shared clipboard page should return 200."""
        response = client.get("/shared-clipboard")
        assert response.status_code == 200


class TestFileNotFound:
    """Tests for 404 handling."""

    def test_nonexistent_upload(self, client):
        """Should return 404 for nonexistent uploaded file."""
        response = client.get("/uploads/nonexistent.txt")
        assert response.status_code == 404

    def test_nonexistent_clipboard_raw(self, client):
        """Should return 404 for nonexistent clipboard raw file."""
        response = client.get("/clipboard/raw/nonexistent.txt")
        assert response.status_code == 404
