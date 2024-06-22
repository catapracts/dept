# Dockerfile for FastAPI server

# Base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set working directory inside the container
WORKDIR /app

# Install dependencies (copy only requirements.txt if you have one)
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory into the container
COPY . /app

# Command to run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

