"""Unit tests for crypto module."""

import pytest

from clipdrop.crypto import (
    KEY_SIZE,
    decrypt_data,
    encrypt_data,
    generate_key,
    generate_key_b64,
    is_likely_encrypted,
    load_key_from_env,
    safe_decrypt,
)


class TestKeyGeneration:
    """Tests for key generation functions."""

    def test_generate_key_returns_correct_length(self):
        """Generated key should be KEY_SIZE bytes."""
        key = generate_key()
        assert len(key) == KEY_SIZE

    def test_generate_key_is_random(self):
        """Each generated key should be unique."""
        key1 = generate_key()
        key2 = generate_key()
        assert key1 != key2

    def test_generate_key_b64_is_valid_base64(self):
        """Base64 key should be decodable."""
        key_b64 = generate_key_b64()
        key = load_key_from_env(key_b64)
        assert len(key) == KEY_SIZE


class TestLoadKeyFromEnv:
    """Tests for loading keys from environment."""

    def test_load_valid_key(self):
        """Should load a valid base64-encoded key."""
        import base64

        original_key = generate_key()
        key_b64 = base64.b64encode(original_key).decode("ascii")
        loaded_key = load_key_from_env(key_b64)
        assert loaded_key == original_key

    def test_load_empty_key_raises(self):
        """Should raise ValueError for empty key."""
        with pytest.raises(ValueError, match="empty"):
            load_key_from_env("")


class TestEncryption:
    """Tests for encryption/decryption functions."""

    def test_encrypt_decrypt_roundtrip(self):
        """Encrypted data should decrypt to original."""
        key = generate_key()
        plaintext = b"Hello, World! This is a test message."

        encrypted = encrypt_data(plaintext, key)
        decrypted = decrypt_data(encrypted, key)

        assert decrypted == plaintext

    def test_encrypted_data_is_different(self):
        """Encrypted data should not equal plaintext."""
        key = generate_key()
        plaintext = b"Secret message"

        encrypted = encrypt_data(plaintext, key)

        assert encrypted != plaintext
        assert plaintext not in encrypted

    def test_encrypt_with_invalid_key_length(self):
        """Should raise ValueError for invalid key length."""
        with pytest.raises(ValueError, match="Key must be"):
            encrypt_data(b"test", b"short-key")

    def test_decrypt_with_wrong_key_fails(self):
        """Decryption with wrong key should fail."""
        key1 = generate_key()
        key2 = generate_key()
        plaintext = b"Secret message"

        encrypted = encrypt_data(plaintext, key1)

        with pytest.raises(Exception):  # InvalidTag or similar
            decrypt_data(encrypted, key2)


class TestIsLikelyEncrypted:
    """Tests for encrypted data detection."""

    def test_plain_text_not_encrypted(self):
        """Plain UTF-8 text should not be detected as encrypted."""
        plain_text = b"This is plain text content."
        assert is_likely_encrypted(plain_text) is False

    def test_pdf_signature_not_encrypted(self):
        """PDF file signature should not be detected as encrypted."""
        pdf_header = b"%PDF-1.4 some content here that is long enough"
        assert is_likely_encrypted(pdf_header) is False

    def test_png_signature_not_encrypted(self):
        """PNG file signature should not be detected as encrypted."""
        png_header = b"\x89PNG\r\n\x1a\n" + b"\x00" * 50
        assert is_likely_encrypted(png_header) is False

    def test_short_data_not_encrypted(self):
        """Data shorter than minimum encrypted size is not encrypted."""
        short_data = b"short"
        assert is_likely_encrypted(short_data) is False


class TestSafeDecrypt:
    """Tests for safe decryption with fallback."""

    def test_safe_decrypt_encrypted_data(self):
        """Should successfully decrypt encrypted data."""
        key = generate_key()
        plaintext = b"Test message for safe decrypt"

        encrypted = encrypt_data(plaintext, key)
        decrypted, was_encrypted = safe_decrypt(encrypted, key)

        assert decrypted == plaintext
        assert was_encrypted is True

    def test_safe_decrypt_plain_text_fallback(self):
        """Should return plain text unchanged if not encrypted."""
        key = generate_key()
        plain_text = b"This is plain text that should pass through."

        result, was_encrypted = safe_decrypt(plain_text, key)

        assert result == plain_text
        assert was_encrypted is False
