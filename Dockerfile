# Use an official Python runtime as a parent image
FROM python:3.9

RUN useradd -ms /bin/bash appuser
USER appuser


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set execute permission for entrypoint.sh
RUN chmod +x entrypoint.sh

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run migrations and start the Django development server
CMD ["./entrypoint.sh"]
