from django.test import TestCase

from menu.models import Menu, Dish


class TestDishModel(TestCase):
    def setUp(self):
        self.object1 = Dish()
        self.object1.name = 'dish 1'
        self.object1.description = 'desc 1'
        self.object1.price = 10.0
        self.object1.preparation_time = 55
        self.object1.is_vege = False
        self.object1.save()

        self.queryset = Dish.objects.all()

    def test_dish_created(self):
        self.assertEquals(len(self.queryset), 1)
        self.assertEquals(self.queryset[0].__str__(), f'{self.object1.name}')


class TestMenuModel(TestCase):
    def setUp(self):
        self.object1 = Menu()
        self.object1.name = 'menu 1'
        self.object1.description = 'desc 1'
        self.object1.save()

        self.queryset = Menu.objects.all()

    def test_menu_created(self):
        self.assertEquals(len(self.queryset), 1)
        self.assertEquals(self.queryset[0].__str__(), f'{self.object1.name}')
