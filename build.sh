#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python alx_travel_app/manage.py collectstatic --no-input

python alx_travel_app/manage.py migrate