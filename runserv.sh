#!/bin/bash

cd venv/bin
source activate
./activate
cd ../..
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py createsuperuser
gnome-terminal -- celery -A eMenu.celery worker
gnome-terminal -- celery -A eMenu beat
python3 manage.py runserver
