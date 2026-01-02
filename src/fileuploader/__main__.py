"""
Entry point for running the application via `python -m fileuploader`.
"""

from fileuploader.app import create_app


def main():
    """Run the Flask development server."""
    app = create_app()
    app.run(host="0.0.0.0", port=3010, debug=True)


if __name__ == "__main__":
    main()
