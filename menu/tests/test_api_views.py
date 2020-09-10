from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory

from menu.models import Menu, Dish

class TestMenuViewSet(APITestCase):
    def setUp(self):
        self.dish = Dish()

        self.dish.name = 'test name'
        self.dish.description = 'test description'
        self.dish.price = 10
        self.dish.preparation_time = 20
        self.dish.is_vege = False
        self.dish.save()

        self.menu1 = Menu()
        self.menu1.name = 'Test menu1'
        self.menu1.description = 'test desc'
        self.menu1.save()

        self.menu2 = Menu()
        self.menu2.name = 'Test menu2'
        self.menu2.description = 'test desc'
        self.menu1.save()

    def test_public_menu_viewset(self):
        queryset = Menu.objects.get(id=self.dish.id)
        queryset.dishes.add(self.dish.id)
        queryset.dishes_count = 1
        queryset.save()

        response = self.client.get('/api/public/menu/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['count'], 1)
