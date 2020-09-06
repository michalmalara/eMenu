from rest_framework import filters
from rest_framework import viewsets

from .models import Menu, Dish
from .serializers import (MenuSerializer, DishSerializer)

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class MenuDetailApiView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    search_fields = ['name']
    filterset_fields = ['created', 'modified', 'dishes']
    ordering_fields = ['created', 'modified']

class DishDetailApiView(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    search_fields = ['name']
    filterset_fields = ['created', 'modified', 'is_vege']
    ordering_fields = ['created', 'modified']
