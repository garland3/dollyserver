# Base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements.txt to container
COPY requirements.txt .
RUN sed -i '/certifi/d' requirements.txt


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files to container
COPY . .

# Set environment variables
# export HF_HOME=/mnt/data/huggingface
# export HUGGINGFACE_HUB_CACHE=/mnt/data/huggingface
ENV HF_HOME=/mnt/data/huggingface
ENV HUGGINGFACE_HUB_CACHE=/mnt/data/huggingface

# Expose port 8005
EXPOSE 8005

WORKDIR /app/src/dollyserver

# make /mnt/data/huggingface a volume
RUN mkdir -p /mnt/data/huggingface

# Start the application
CMD ["uvicorn", "dolly2_api:app", "--host", "0.0.0.0", "--port", "8005"]
