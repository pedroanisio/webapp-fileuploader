"""
Shared helper functions and constants for ClipDrop.

This module consolidates common functionality to avoid code duplication (DRY).
"""

from datetime import datetime, timedelta, timezone

from flask import jsonify

from clipdrop.crypto import encrypt_data, safe_decrypt

# =============================================================================
# Constants
# =============================================================================

ALLOWED_EXTENSIONS = {
    "txt",
    "pdf",
    "png",
    "jpg",
    "jpeg",
    "gif",
    "pst",
    "md",
    "json",
    "zip",
    "tar",
    "py",
    "html",
    "css",
}

MIMETYPE_MAP = {
    "txt": "text/plain",
    "pdf": "application/pdf",
    "png": "image/png",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "gif": "image/gif",
    "json": "application/json",
    "html": "text/html",
    "css": "text/css",
    "md": "text/markdown",
    "py": "text/x-python",
    "zip": "application/zip",
    "tar": "application/x-tar",
}

OAUTH_ERROR_MESSAGES = {
    "bad_verification_code": "The login code has expired. Please try signing in again.",
    "access_denied": "GitHub access was denied. Please try again.",
    "invalid_grant": "The authorization code has expired. Please try signing in again.",
    "incorrect_client_credentials": "OAuth configuration error. Please contact the administrator.",
}


# =============================================================================
# JSON Response Helpers
# =============================================================================


def json_error(message: str, status_code: int = 400):
    """Create a JSON error response.

    Args:
        message: Error message to return
        status_code: HTTP status code (default 400)

    Returns:
        Tuple of (response, status_code)
    """
    return jsonify({"status": "error", "message": message}), status_code


def json_success(message: str, **kwargs):
    """Create a JSON success response.

    Args:
        message: Success message to return
        **kwargs: Additional data to include in response

    Returns:
        JSON response object
    """
    payload = {"status": "success", "message": message}
    payload.update(kwargs)
    return jsonify(payload)


# =============================================================================
# Encryption Helpers
# =============================================================================


def encrypt_data_safe(data: bytes, key: bytes | None) -> bytes:
    """Encrypt data if encryption key is available.

    Args:
        data: Raw bytes to encrypt
        key: Encryption key (32 bytes) or None

    Returns:
        Encrypted data if key provided, otherwise original data
    """
    if key:
        return encrypt_data(data, key)
    return data


def decrypt_data_safe(data: bytes, key: bytes | None) -> bytes:
    """Decrypt data if encrypted.

    Args:
        data: Potentially encrypted data
        key: Encryption key (32 bytes) or None

    Returns:
        Decrypted data if key provided, otherwise original data
    """
    if key:
        decrypted, _ = safe_decrypt(data, key)
        return decrypted
    return data


# =============================================================================
# Expiration Helpers
# =============================================================================


def calculate_expiry(keep: bool, days: int = 1) -> datetime | None:
    """Calculate expiration date based on retention setting.

    Args:
        keep: If True, return None (no expiration)
        days: Number of days until expiration (default 1)

    Returns:
        Expiration datetime or None if keep=True
    """
    if keep:
        return None
    return datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(days=days)


# =============================================================================
# OAuth Helpers
# =============================================================================


def get_oauth_error_message(error_type: str) -> str:
    """Get user-friendly OAuth error message.

    Args:
        error_type: OAuth error type string

    Returns:
        User-friendly error message
    """
    return OAUTH_ERROR_MESSAGES.get(
        error_type, "Authentication failed. Please try again."
    )


# =============================================================================
# File Helpers
# =============================================================================


def get_file_extension(filename: str) -> str:
    """Get file extension from filename.

    Args:
        filename: Name of file

    Returns:
        Lowercase file extension or empty string
    """
    if "." in filename:
        return filename.rsplit(".", 1)[1].lower()
    return ""


def human_readable_size(size_bytes: int | float) -> str:
    """Convert bytes to human readable format.

    Args:
        size_bytes: Size in bytes

    Returns:
        Human readable string (e.g., "1.5 MB")
    """
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


def allowed_file(filename: str) -> bool:
    """Check if a file extension is allowed.

    Args:
        filename: Name of file to check

    Returns:
        True if extension is in ALLOWED_EXTENSIONS
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
