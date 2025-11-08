# --- Dockerfile for Frog App on Fly.io ---
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your code and assets
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that NiceGUI runs on
EXPOSE 8080

# Command to run the app
CMD ["python", "main2.py"]
