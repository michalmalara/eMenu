from rest_framework import serializers

from menu.models import Menu, Dish


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        read_only_fields = ['dishes_count']


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'

