#!/usr/bin/env bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py migrate --noinput


echo "Collecting static files..."
python manage.py collectstatic --noinput
