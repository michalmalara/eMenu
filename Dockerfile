FROM python:3.8.2

ENV PYTHONUNBUFFERRED 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py makemigrations

RUN python manage.py migrate

RUN python manage.py loaddata fixtures.json
