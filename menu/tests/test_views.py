from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from django.urls import reverse

from menu.models import Menu, Dish


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        test_user1 = User.objects.create_user(username='testuser1', password='abcd')

        self.menu1 = Menu()
        self.menu1.name = 'menu1'
        self.menu1.description = 'opis1'
        self.menu1.save()

        self.dish1 = Dish()
        self.dish1.name = 'danie 1'
        self.dish1.description = 'opis1'
        self.dish1.price = 100
        self.dish1.preparation_time = 55
        self.dish1.is_vege=False
        self.dish1.save()

        self.menu_queryset = Menu.objects.all()
        self.dish_queryset = Dish.objects.all()

        self.menu_queryset[0].dishes.set(self.dish_queryset)

        test_user1.save()

    def test_home_view(self):
        homeUrl = reverse('home')
        response = self.client.get(homeUrl)
        self.assertEquals(response.status_code, 200)

    def test_menu_detail_view(self):
        url = reverse('menu_detail', args=[self.menu_queryset[0].pk])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # def test_user_not_logged_in(self):
    #     response = self.client.get(self.homeUrl)
    #     self.assertEquals(response.status_code, 302)
