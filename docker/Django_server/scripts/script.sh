#!/bin/sh

python manage.py migrate

# collects all static files in our app and puts it in the STATIC_ROOT
python manage.py collectstatic --noinput

python manage.py runserver 0.0.0.0:8000