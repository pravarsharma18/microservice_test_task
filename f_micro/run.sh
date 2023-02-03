#!/bin/bash

RUN_PORT=${PORT:-8001}
/opt/venv-flask/bin/gunicorn --workers=2 --bind=0.0.0.0:$RUN_PORT app:app