#!/bin/sh

echo "Migrating database..."
# EN CAS DE PB - HARD RESET
# python3.9 manage.py flush --noinput
# python3.9 manage.py migrate portfolio zero --noinput

python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Create cache table..."
python3.9 manage.py createcachetable

echo "Creating superuser..."

DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

python3.9 manage.py createsuperuser \
  --email $DJANGO_SUPERUSER_EMAIL \
  --noinput || true

echo "Collecting static files..."
python3.9 manage.py collectstatic -i rest_framework -i flags --noinput --clear

echo "Starting app server..."
python -m gunicorn portfolio.wsgi:application \
  --bind 0.0.0.0:8000 \
  --log-level info \
  --config gunicorn.cfg.py \
  --forwarded-allow-ips "*"
