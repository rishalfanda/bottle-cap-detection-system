# Gunakan image Python yang ringan
FROM python:3.10-slim

# Install library sistem untuk OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy file requirements dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh source code
COPY . .

# Install paket bsort ke dalam sistem container
RUN pip install .

# Perintah default saat container jalan
CMD ["bsort", "--help"]