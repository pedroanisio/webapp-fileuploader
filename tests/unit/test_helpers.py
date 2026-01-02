"""Tests for helper functions module."""

from datetime import datetime, timedelta, timezone

import pytest


class TestJsonResponses:
    """Tests for JSON response helper functions."""

    def test_json_error_default_status(self, app):
        from clipdrop.helpers import json_error

        with app.app_context():
            response, status = json_error("Something went wrong")
            assert status == 400
            assert response.json["status"] == "error"
            assert response.json["message"] == "Something went wrong"

    def test_json_error_custom_status(self, app):
        from clipdrop.helpers import json_error

        with app.app_context():
            response, status = json_error("Not found", 404)
            assert status == 404
            assert response.json["status"] == "error"
            assert response.json["message"] == "Not found"

    def test_json_success_simple(self, app):
        from clipdrop.helpers import json_success

        with app.app_context():
            response = json_success("Operation completed")
            assert response.json["status"] == "success"
            assert response.json["message"] == "Operation completed"

    def test_json_success_with_extra_data(self, app):
        from clipdrop.helpers import json_success

        with app.app_context():
            response = json_success("Created", id="abc123", name="test")
            assert response.json["status"] == "success"
            assert response.json["message"] == "Created"
            assert response.json["id"] == "abc123"
            assert response.json["name"] == "test"


class TestEncryption:
    """Tests for unified encryption/decryption functions."""

    def test_encrypt_data_with_key(self):
        from clipdrop.helpers import encrypt_data_safe

        # Without key, returns original data
        data = b"hello world"
        result = encrypt_data_safe(data, None)
        assert result == data

    def test_encrypt_data_with_valid_key(self):
        import os

        from clipdrop.helpers import decrypt_data_safe, encrypt_data_safe

        key = os.urandom(32)
        data = b"secret message"
        encrypted = encrypt_data_safe(data, key)
        assert encrypted != data

        # Should be able to decrypt
        decrypted = decrypt_data_safe(encrypted, key)
        assert decrypted == data

    def test_decrypt_data_without_key(self):
        from clipdrop.helpers import decrypt_data_safe

        data = b"plain text"
        result = decrypt_data_safe(data, None)
        assert result == data


class TestExpirationCalculation:
    """Tests for expiration date calculation."""

    def test_calculate_expiry_keep_true(self):
        from clipdrop.helpers import calculate_expiry

        result = calculate_expiry(keep=True)
        assert result is None

    def test_calculate_expiry_keep_false(self):
        from clipdrop.helpers import calculate_expiry

        before = datetime.now(timezone.utc)
        result = calculate_expiry(keep=False)
        after = datetime.now(timezone.utc)

        assert result is not None
        expected_min = before + timedelta(days=1)
        expected_max = after + timedelta(days=1)
        # Compare without timezone for compatibility
        assert expected_min.replace(tzinfo=None) <= result <= expected_max.replace(tzinfo=None)

    def test_calculate_expiry_custom_days(self):
        from clipdrop.helpers import calculate_expiry

        before = datetime.now(timezone.utc)
        result = calculate_expiry(keep=False, days=7)
        after = datetime.now(timezone.utc)

        assert result is not None
        expected_min = before + timedelta(days=7)
        expected_max = after + timedelta(days=7)
        # Compare without timezone for compatibility
        assert expected_min.replace(tzinfo=None) <= result <= expected_max.replace(tzinfo=None)


class TestOAuthErrorMessages:
    """Tests for OAuth error message constants."""

    def test_oauth_error_messages_exists(self):
        from clipdrop.helpers import OAUTH_ERROR_MESSAGES

        assert isinstance(OAUTH_ERROR_MESSAGES, dict)
        assert "bad_verification_code" in OAUTH_ERROR_MESSAGES
        assert "access_denied" in OAUTH_ERROR_MESSAGES

    def test_get_oauth_error_message_known(self):
        from clipdrop.helpers import get_oauth_error_message

        msg = get_oauth_error_message("bad_verification_code")
        assert "expired" in msg.lower() or "login" in msg.lower()

    def test_get_oauth_error_message_unknown(self):
        from clipdrop.helpers import get_oauth_error_message

        msg = get_oauth_error_message("unknown_error_type")
        assert "failed" in msg.lower() or "try again" in msg.lower()


class TestFileHelpers:
    """Tests for file-related helper functions."""

    def test_get_file_extension(self):
        from clipdrop.helpers import get_file_extension

        assert get_file_extension("test.txt") == "txt"
        assert get_file_extension("image.PNG") == "png"
        assert get_file_extension("no_extension") == ""
        assert get_file_extension("multi.part.name.pdf") == "pdf"

    def test_human_readable_size(self):
        from clipdrop.helpers import human_readable_size

        assert human_readable_size(500) == "500.0 B"
        assert human_readable_size(1024) == "1.0 KB"
        assert human_readable_size(1024 * 1024) == "1.0 MB"
        assert human_readable_size(1024 * 1024 * 1024) == "1.0 GB"

    def test_allowed_file(self):
        from clipdrop.helpers import allowed_file

        assert allowed_file("test.txt") is True
        assert allowed_file("image.png") is True
        assert allowed_file("script.exe") is False
        assert allowed_file("noextension") is False
