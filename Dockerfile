FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# CRITICAL: Install crypto libraries in correct order
RUN pip install --upgrade pip && \
    pip uninstall -y pycrypto pycryptodome || true && \
    pip install --no-cache-dir pycryptodome>=3.15.0 && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

EXPOSE 8080

CMD ["python3", "main.py"]
