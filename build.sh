#!/usr/bin/env bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py migrate --noinput

echo "Creating superuser..."
python manage.py shell < create_superuser.py

echo "Collecting static files..."
python manage.py collectstatic --noinput
