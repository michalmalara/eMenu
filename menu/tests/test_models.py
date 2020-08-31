import datetime

from django.test import TestCase

from menu.models import Menu, Dish


class TestMenuModel(TestCase):
    def setUp(self):
        self.object1 = Menu()
        self.object1.name = 'Danie1'
        self.object1.description = 'Opis1'
        self.object1.save()

        self.queryset = Menu.objects.all()

    def test_menu_created(self):
        self.assertEquals(len(self.queryset), 1)
        self.assertEquals(self.queryset[0].name, self.object1.name)
        self.assertEquals(self.queryset[0].description, self.object1.description)
        self.assertEquals(self.queryset[0].created, self.object1.created)
        self.assertEquals(self.queryset[0].modified, self.object1.modified)


class TestDishModel(TestCase):
    def setUp(self):
        self.object1 = Dish()
        self.object1.name = 'Danie1'
        self.object1.description= 'Opis1'
        self.object1.price = 10.0
        self.object1.prepare_time = 55
        self.object1.is_vege = False
        self.object1.save()

        self.queryset = Dish.objects.all()

    def test_dish_created(self):
        self.assertEquals(len(self.queryset), 1)
