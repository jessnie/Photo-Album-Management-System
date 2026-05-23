#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate --noinput

echo "Build completed successfully!"
echo "Note: Create a superuser manually after first deployment"
echo "Command: python manage.py createsuperuser"