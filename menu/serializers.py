from rest_framework import serializers

from menu.models import Menu, Dish


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

    def get_dishes_count(self, obj):
        return obj.dishes.count()


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
