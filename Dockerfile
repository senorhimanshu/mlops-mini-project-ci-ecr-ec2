# Use lightweight Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy the entire application (Flask app, scripts, etc.)
COPY flask_app/ /app/

COPY scripts/download_model.py /app/scripts/download_model.py

COPY models/vectorizer.pkl /app/models/vectorizer.pkl

# Copy only the essential project files first (for caching efficiency)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install NLTK resources
RUN python -m nltk.downloader stopwords wordnet

# Expose Flask port
EXPOSE 5000

# Run app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]