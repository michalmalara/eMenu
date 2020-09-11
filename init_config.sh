#!/bin/bash

cd venv/bin
source activate
./activate
cd ../..
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py createsuperuser