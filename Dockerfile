# Use a lightweight Python image as the base
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the working directory
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the port on which the Django app will run
EXPOSE 8000

# Command to run when the container starts
CMD ["python", "manage.py", "runserver"]