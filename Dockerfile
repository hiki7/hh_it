# Use Python 3.12 as the base image for requirements
FROM python:3.12 AS requirements-stage

# Set the working directory for installing dependencies
WORKDIR /tmp

# Install Poetry for dependency management
RUN pip install poetry==1.5.0

# Copy dependency files and install dependencies directly with Poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Final stage
FROM python:3.12

# Update and install necessary system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory for the application code
WORKDIR /hh_it

# Copy installed dependencies from the previous stage
COPY --from=requirements-stage /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=requirements-stage /usr/local/bin /usr/local/bin

# Copy the entire project into the Docker image
COPY . .

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=hh_it.settings \
    PYTHONUNBUFFERED=1

# Expose the port on which Django will run
EXPOSE 8000

# Start the Django development server by default
CMD ["python", "hh_it/manage.py", "runserver", "0.0.0.0:8000"]
