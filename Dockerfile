# Minimal python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy a file with a list of requirements 
COPY requirements.txt .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY static/ /app/static
COPY templates/ /app/templates
COPY weather.py /app/app.py

# Env. variables for flask
ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000

# specify the port that the application will use
EXPOSE 5000

# define  ENTRYPOINT to run the command
ENTRYPOINT ["python"]

# Define the default command for the application
CMD ["weather.py"]
