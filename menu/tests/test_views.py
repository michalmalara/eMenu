from django.contrib.auth.models import User
from django.db.models.functions import datetime
from django.test import TestCase, RequestFactory
from django.test import Client
from django.urls import reverse

from menu.models import Menu, Dish
from menu.views import param_replace, MenuCreateView


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.test_user1 = User.objects.create_user(username='testuser1', password='abcd')
        self.test_user1.save()

        for i in range(50):
            self.menu1 = Menu()
            self.menu1.name = f'menu {i}'
            self.menu1.description = f'opis{i}'
            self.menu1.save()

        for i in range(50):
            self.dish1 = (Dish())
            self.dish1.name = f'danie {i}'
            self.dish1.description = f'opis {i}'
            self.dish1.price = i
            self.dish1.preparation_time = i + 12
            if i // 3 == 0:
                self.dish1.is_vege = True
            else:
                self.dish1.is_vege = False

            self.dish1.save()

        self.menu_queryset = Menu.objects.all()
        self.dish_queryset = Dish.objects.all()

        self.menu_queryset[0].dishes.set(self.dish_queryset)

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_view_pagination(self):
        url = reverse('home')
        response = self.client.get(url)

        for i in range(10):
            self.assertContains(response, f'menu {i}')

        response = self.client.get(url + '?page=2')
        for i in range(10, 20):
            self.assertContains(response, f'menu {i}')

    def test_home_view_searching(self):
        url = reverse('home')

        response = self.client.get(url + '?name=24')
        self.assertContains(response, 'menu 24')

        response = self.client.get(url + '?name=24')
        self.assertContains(response, 'menu 24')

        response = self.client.get(url + '?sorting=name&sorting_direction=ASC')
        self.assertContains(response, 'menu 1')

        response = self.client.get(url + '?sorting=name&sorting_direction=DESC')
        self.assertContains(response, 'menu 49')

    #     TODO: test created_starting_date, created_ending_date, edited_starting_date, edited_ending_date

    def test_menu_detail_view(self):
        url = reverse('menu_detail', args=[self.menu_queryset[0].pk])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_dish_detail_view(self):
        url = reverse('dish_detail', args=[self.menu_queryset[0].pk])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_param_replace(self):
        factory = RequestFactory()
        request = factory.get('/?sort_by=name&ascending=true')
        context = {'request': request}
        func_resp = param_replace(context)

        self.assertEquals(func_resp, 'sort_by=name&ascending=true')

    def test_user_not_logged_in(self):
        url = reverse('create_menu')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_create_menu(self):
        url = reverse('create_menu')
        self.client.login(username='testuser1', password='abcd')
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

    def test_menu_is_created(self):
        url = reverse('create_menu')
        self.client.login(username='testuser1', password='abcd')
        response = self.client.post(url, {'name': 'test menu', 'description': 'test desc'})
        queryset = Menu.objects.all()
        self.assertEquals(response.status_code, 200)

        self.assertEquals(queryset[50].name, 'test menu')
        self.assertEquals(queryset[50].description, 'test desc')
