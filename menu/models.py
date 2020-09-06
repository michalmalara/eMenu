from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.signals import request_finished

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nazwa')
    description = models.TextField(max_length=1000, verbose_name='Opis')
    price = models.FloatField(verbose_name='Cena')
    preparation_time = models.IntegerField(verbose_name='Czas przygotowania')
    is_vege = models.BooleanField(verbose_name='Danie wegetariańskie')
    picture = models.ImageField(default = 'default.jpg',verbose_name='Zdjęcie dania')
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
    name = models.CharField(max_length=50, unique=True, verbose_name='Nazwa')
    description = models.TextField(max_length=1000, verbose_name='Opis')
    created = models.DateTimeField(editable=False, verbose_name='Utworzono')
    modified = models.DateTimeField(auto_now=True, verbose_name='Zmodyfikowano')
    dishes = models.ManyToManyField(Dish, blank=True, verbose_name='Dania', related_name='menus')
    dishes_length = models.IntegerField(default=0, verbose_name='Liczba dań w karcie')

    def __str__(self):
        return f'{self.name}: {self.dishes.count()}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Menu, self).save(*args, **kwargs)


# SIGNALS

@receiver(post_save, sender=Menu)
def count_dishes_in_menu(sender, **kwargs):
    kwargs['instance'].dishes_length = kwargs['instance'].dishes.count()

    print(kwargs['instance'].dishes_length)



request_finished.connect(count_dishes_in_menu, sender=Menu, dispatch_uid="count_dishes_in_menu_identifier")