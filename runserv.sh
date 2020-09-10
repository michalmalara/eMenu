#!/bin/bash

cd venv/bin
source activate
./activate
cd ../..
gnome-terminal -- celery -A eMenu.celery worker
gnome-terminal -- celery -A eMenu beat
python3 manage.py runserver
