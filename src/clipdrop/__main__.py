"""
Entry point for running the application via `python -m clipdrop`.
"""

import os
from clipdrop.app import create_app


def main():
    """Run the Flask development server."""
    port = int(os.getenv("PORT", "3000"))
    debug = os.getenv("FLASK_DEBUG", "false").lower() in ("true", "1", "yes")
    app = create_app()
    app.run(host="0.0.0.0", port=port, debug=debug)


if __name__ == "__main__":
    main()
