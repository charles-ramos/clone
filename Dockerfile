# Use the official Python image as the base image
FROM python:3.10.0a6-alpine3.13

# Set the working directory in the container
WORKDIR /clone

# Copy the application files into the working directory
COPY . /clone

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["python", "app.py"]