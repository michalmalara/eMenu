from django.test import TestCase
from menu.models import Menu

class TestModel(TestCase):
    def test_menu_created(self):
        object1 = Menu()
        object1.name = 'Danie1'
        object1.description = 'Opis1'
        object1.save()

        queryset = Menu.objects.all()

        self.assertEquals(len(queryset), 1)