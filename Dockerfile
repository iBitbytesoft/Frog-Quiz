FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port
EXPOSE 8080

# Run the application (main_web.py is the NiceGUI web app, main.py is the Kivy APK app)
CMD ["python", "main_web.py"]
