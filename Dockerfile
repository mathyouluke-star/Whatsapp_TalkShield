
---

## 📄 `Dockerfile`
#If you prefer containerised deployment (Render supports both Procfile and Dockerfile):

#```dockerfile
# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy app
COPY . .

# Expose port
EXPOSE 5000

# Start the service
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
