import datetime

from django.test import TestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from menu.models import Menu, Dish
from menu.serializers import MenuSerializer, DishSerializer


class TestMenuSerializer(TestCase):
    def setUp(self):
        self.menu_attributes = {
            'name': 'Test name',
            'description': 'Test description',
        }

        self.serializer_data = {
            'name': 'Test name 1',
            'description': 'Test description 1',
        }

        self.factory = APIRequestFactory()
        self.request = self.factory.get('api/menu/')

        self.serializer_context = {
            'request': Request(self.request),
        }

        self.menu = Menu.objects.create(**self.menu_attributes)
        self.serializer = MenuSerializer(instance=self.menu, context=self.serializer_context)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertCountEqual(
            data.keys(),
            [
                'url',
                'name',
                'description',
                'created',
                'modified',
                'dishes',
                'dishes_count'
            ]
        )

    def test_content(self):
        data = self.serializer.data

        self.assertEquals(data['name'], self.menu.name)
        self.assertEquals(data['description'], self.menu.description)
        self.assertCountEqual(data['dishes'], self.menu.dishes.all())

    def test_validation(self):
        self.serializer_data['name'] = 'Nazwa update'

        serializer = MenuSerializer(data=self.serializer_data)
        serializer.is_valid()

        new_menu = serializer.save()
        new_menu.refresh_from_db()

        self.assertEqual(new_menu.name, 'Nazwa update')



class TestDishSerializer(TestCase):
    def setUp(self):
        self.dish_attributes = {
            'name': 'Test name',
            'description': 'Test description',
            'price': 100,
            'preparation_time': 60,
            'is_vege': False,
        }

        self.serializer_data = {
            'name': 'Test name 1',
            'description': 'Test description 1',
            'price': 110,
            'preparation_time': 65,
            'is_vege': True,
        }

        self.dish = Dish.objects.create(**self.dish_attributes)
        self.serializer = DishSerializer(instance=self.dish)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertCountEqual(
            data.keys(),
            [
                'id',
                'name',
                'description',
                'price',
                'preparation_time',
                'is_vege',
                'picture',
                'created',
                'modified'
            ]
        )

    def test_content(self):
        data = self.serializer.data

        self.assertEquals(data['name'], self.dish.name)
        self.assertEquals(data['description'], self.dish.description)
        self.assertEquals(data['price'], self.dish.price)
        self.assertEquals(data['preparation_time'], self.dish.preparation_time)
        self.assertEquals(data['is_vege'], self.dish.is_vege)
        self.assertEquals(data['picture'], self.dish.picture.url)

    def test_validation(self):
        self.serializer_data['name'] = 'Nazwa update'

        serializer = DishSerializer(data=self.serializer_data)
        serializer.is_valid()

        new_dish = serializer.save()
        new_dish.refresh_from_db()

        self.assertEqual(new_dish.name, 'Nazwa update')