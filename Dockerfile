# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app
ENV PYTHONPATH=/app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY backend .

# Set environment variables
ENV FLASK_APP=flask_app.py
ENV FLASK_ENV=production

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"] 