from django.db import models
from django.db.models import Count
from django.utils import timezone


# Create your models here.

class Dish(models.Model):
    name = models.TextField(max_length=50, unique=True)
    description = models.TextField(max_length=1000)
    price = models.FloatField()
    preparation_time = models.IntegerField()
    is_vege = models.BooleanField()
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Dish, self).save(*args, **kwargs)


class Menu(models.Model):
    name = models.TextField(max_length=50, unique=True)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(auto_now=True)
    dishes = models.ManyToManyField(Dish)

    def __str__(self):
        return f'{self.name}: {self.dishes.count()}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Menu, self).save(*args, **kwargs)

