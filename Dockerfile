# Use an Alpine-based Python 3.8 image as the base image
FROM python:3.8-alpine

# Upgrade all packages in the Alpine image to their latest versions
RUN apk --no-cache upgrade

# Add a non-privileged user called gpt-answers to run the application
RUN adduser -D gtt

# Set the working directory of the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the /app directory in the container
COPY src /app

# Change the ownership of the /app directory to the non-privileged user
RUN chown -R gtt:gtt /app

# Set the user to run the application as gpt-answers
USER gtt

# Start the application using the command "python app.py"
CMD ["python", "app.py"]

# Expose port 5000 to allow external connections to the container
EXPOSE 5000