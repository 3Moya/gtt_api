# Use a Python 3.9 image as the base image
FROM python:3.9-slim-bullseye

# Set the working directory of the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the /app directory in the container
COPY src /app

# Start the application using the command "python app.py"
CMD ["python", "app.py"]

# Expose port 5000 to allow external connections to the container
EXPOSE 5000