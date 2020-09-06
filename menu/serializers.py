from rest_framework import serializers

from menu.models import Menu, Dish


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        read_only_fields = ['dishes_count']

    def update(self, instance, validated_data):
        print(instance.dishes_count)
        print(len(validated_data['dishes']))
        instance.dishes_count = len(validated_data['dishes'])
        return super().update(instance, validated_data)

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
