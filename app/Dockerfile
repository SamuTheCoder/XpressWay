# Use an official Python runtime as a parent image
FROM python:3.12.3

# Set the working directory in the container
WORKDIR ./app

# Copy only the necessary files for dependency installation
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE ${BACKEND_PORT}
# Set the PYTHONPATH to include the /app directory
ENV PYTHONPATH=/app
# Set environment variables for Flask
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=${BACKEND_HOST}
ENV FLASK_RUN_PORT=${BACKEND_PORT}

# Run the application
CMD ["flask", "run"]