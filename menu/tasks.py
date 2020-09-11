from __future__ import absolute_import, unicode_literals

import datetime

from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.datetime_safe import date

from menu.models import Dish, Menu


@shared_task
def send_email():
    dishes = Dish.objects.filter(modified__gte=(date.today() - datetime.timedelta(days=1)))
    menus = Menu.objects.filter(modified__gte=(date.today() - datetime.timedelta(days=1)))

    users = User.objects.all()

    for user in users:
        html_message = render_to_string('email_template.html',
                                        {'host_url': 'http://127.0.0.1:8000/',
                                         'dishes': dishes,
                                         'menus': menus,
                                         'username': user.username
                                         },
                                        )
        email = EmailMultiAlternatives(
            subject='eMenu - najnowsze informacje',
            from_email='michalmalaradjangotest@gmail.com',
            to=(user.email, ),
        )
        email.attach_alternative(html_message, "text/html")
        email.send()