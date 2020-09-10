from django.db import models
from django.utils import timezone
from django.db.models.signals import m2m_changed

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
    dishes = models.ManyToManyField(Dish, blank=True, verbose_name='Dania')
    dishes_count = models.IntegerField(default=0, verbose_name='Liczba dań w karcie', editable=False)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Menu, self).save(*args, **kwargs)

# def dishes_changed(sender, **kwargs):
#         if (kwargs['action']=='post_add') or (kwargs['action']=='post_remove'):
#             queryset = Menu.objects.get(pk=kwargs['instance'].pk)
#             queryset.dishes_count = queryset.dishes.count()
#             queryset.save()
#
# m2m_changed.connect(dishes_changed, sender=Menu.dishes.through)


