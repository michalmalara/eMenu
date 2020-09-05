#!/bin/bash

cd venv/bin
source activate
./activate
cd ../..
python3 manage.py runserver
