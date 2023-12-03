# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . .

# Run Django migrations to create the necessary tables in the database
# RUN python manage.py migrate

# Expose the default Django port
EXPOSE 8000

# Start the Django development server
ENTRYPOINT ["/app/app.sh"]