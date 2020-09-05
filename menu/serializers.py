from rest_framework import serializers

from menu.models import Menu, Dish


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    dishes = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Menu
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dish
        fields = '__all__'
