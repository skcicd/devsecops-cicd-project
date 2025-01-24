# Base image with Python 3.9
# 'slim' version reduces image size
FROM python:3.9-slim
# Sets working directory inside container
WORKDIR /app
# Copies dependency file into container
COPY requirements.txt .
# Installs Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copies entire project into container
COPY . .
# Indicates container will listen on port 5000
EXPOSE 5000
# Command to start Flask application when container runs
CMD ["python", "src/app.py"]
