# Use a slim version of Python 3.9 as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the consumer script to the working directory
COPY consumer.py consumer.py

# Specify the command to run the consumer script
CMD ["python", "consumer.py"]
