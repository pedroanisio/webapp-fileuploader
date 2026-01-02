# Use the official Python image from Docker Hub
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy pyproject.toml and install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Copy the source code
COPY src/ src/
COPY scripts/ scripts/

# Copy and run the script to generate the .env file if it doesn't exist
RUN chmod +x scripts/generate_secret.sh && ./scripts/generate_secret.sh

# Create directories for runtime data
RUN mkdir -p uploads clipboard

# Make port 3010 available to the world outside this container
EXPOSE 3010

# Run the application with gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:3010", "fileuploader.app:create_app()"]
