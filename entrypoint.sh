#!/bin/bash
# entrypoint.sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Make migrations and apply them
echo "Running migrations..."
python hh_it/manage.py makemigrations --noinput
python hh_it/manage.py migrate --noinput

# Start the development server
echo "Starting Django development server..."
exec "$@"
