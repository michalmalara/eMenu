# Generated by Django 3.1 on 2020-09-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_remove_menu_dishes_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='dishes_length',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
