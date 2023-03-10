#!/bin/bash

/opt/venv-django/bin/python manage.py migrate --noinput

/opt/venv-django/bin/python manage.py createsuperuser --noinput

/opt/venv-django/bin/python manage.py collectstatic --noinput

RUN_PORT_DJANGO=${PORT:-8002}
/opt/venv-django/bin/gunicorn dj_micro.wsgi:application --bind "0.0.0.0:${RUN_PORT_DJANGO}"