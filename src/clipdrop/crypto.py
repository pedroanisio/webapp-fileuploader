"""
Encryption utilities for data-at-rest protection.
Uses AES-256-GCM for authenticated encryption.
"""

import base64
import os

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

NONCE_SIZE = 12  # 96 bits for GCM (recommended)
KEY_SIZE = 32  # 256 bits for AES-256

# Magic bytes for common file types (used for legacy file detection)
FILE_SIGNATURES = {
    b"%PDF": "pdf",
    b"\x89PNG": "png",
    b"\xff\xd8\xff": "jpg",
    b"GIF87a": "gif",
    b"GIF89a": "gif",
    b"PK\x03\x04": "zip",
    b"!<arch>": "pst",
}


def generate_key() -> bytes:
    """Generate a new 256-bit encryption key."""
    return os.urandom(KEY_SIZE)


def generate_key_b64() -> str:
    """Generate a new 256-bit encryption key as base64 string."""
    return base64.b64encode(generate_key()).decode("ascii")


def load_key_from_env(env_value: str) -> bytes:
    """Load encryption key from base64-encoded environment variable."""
    if not env_value:
        raise ValueError("Encryption key is empty")
    return base64.b64decode(env_value)


def encrypt_data(plaintext: bytes, key: bytes) -> bytes:
    """
    Encrypt data with AES-256-GCM.

    Returns: nonce (12 bytes) + ciphertext + auth tag (16 bytes)
    """
    if not key or len(key) != KEY_SIZE:
        raise ValueError(f"Key must be {KEY_SIZE} bytes")

    nonce = os.urandom(NONCE_SIZE)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return nonce + ciphertext


def decrypt_data(encrypted: bytes, key: bytes) -> bytes:
    """
    Decrypt AES-256-GCM data.

    Expects: nonce (12 bytes) + ciphertext + auth tag (16 bytes)
    Raises InvalidTag if data is corrupted or key is wrong.
    """
    if not key or len(key) != KEY_SIZE:
        raise ValueError(f"Key must be {KEY_SIZE} bytes")

    if len(encrypted) < NONCE_SIZE + 16:  # Minimum: nonce + auth tag
        raise ValueError("Encrypted data too short")

    nonce = encrypted[:NONCE_SIZE]
    ciphertext = encrypted[NONCE_SIZE:]
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ciphertext, None)


def is_likely_encrypted(data: bytes) -> bool:
    """
    Heuristic to detect if data is likely encrypted (for legacy file support).

    Returns True if data appears to be encrypted, False if it looks like
    a plaintext file (has known file signature or valid UTF-8 text).
    """
    if len(data) < NONCE_SIZE + 16:
        # Too short to be encrypted with our scheme
        return False

    # Check for common file magic bytes (plaintext files)
    for signature in FILE_SIGNATURES:
        if data.startswith(signature):
            return False

    # Check if it looks like valid UTF-8 text (for .txt files)
    try:
        # Only check first 1KB to avoid memory issues with large files
        sample = data[:1024]
        sample.decode("utf-8")
        # If it's valid UTF-8 and starts with printable chars, likely plaintext
        if sample and all(c >= 0x20 or c in (0x09, 0x0A, 0x0D) for c in sample[:100]):
            return False
    except UnicodeDecodeError:
        pass

    return True


def safe_decrypt(data: bytes, key: bytes) -> tuple[bytes, bool]:
    """
    Attempt to decrypt data, falling back to raw data for legacy files.

    Returns: (decrypted_or_raw_data, was_encrypted)
    """
    if not is_likely_encrypted(data):
        return data, False

    try:
        decrypted = decrypt_data(data, key)
        return decrypted, True
    except (InvalidTag, ValueError):
        # Decryption failed - treat as unencrypted legacy file
        return data, False
