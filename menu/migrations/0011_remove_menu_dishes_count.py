# Generated by Django 3.1 on 2020-09-06 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_menu_dishes_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='dishes_count',
        ),
    ]
