import os

from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eMenu.settings')

app = Celery('eMenu')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-email-everyday': {
        'task': 'menu.tasks.send_email',
        'schedule': crontab(hour='10', minute='0'),
    },
}

app.conf.timezone = 'Europe/Warsaw'