import rest_framework
from rest_framework import viewsets, permissions

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
    """
    Private viewset for reading, creating, updating and deleting objects in Menu table. Only for logged in users.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [rest_framework.permissions.IsAuthenticated]
    search_fields = ['name']
    filterset_fields = ['created', 'modified', 'dishes']
    ordering_fields = ['created', 'modified', 'dishes_count']


class DishDetailApiView(viewsets.ModelViewSet):
    """
    Private viewset for reading, creating, updating and deleting objects in Dish table. Only for logged in users.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [rest_framework.permissions.IsAuthenticated]
    search_fields = ['name']
    filterset_fields = ['created', 'modified', 'is_vege']
    ordering_fields = ['created', 'modified']

class MenuListPublicApiView(viewsets.ReadOnlyModelViewSet):
    """
    Public viewset for reading Menu table by GET method only.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = []
    search_fields = ['name']
    filterset_fields = ['created', 'modified', 'dishes']
    ordering_fields = ['created', 'modified', 'dishes_count']


class DishDetailPublicApiView(viewsets.ReadOnlyModelViewSet):
    """
    Public viewset for reading Dish table by GET method only.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = []
    search_fields = ['name']
    filterset_fields = ['created', 'modified', 'is_vege']
    ordering_fields = ['created', 'modified']
