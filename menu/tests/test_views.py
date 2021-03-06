from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.test import Client
from django.urls import reverse

from menu.models import Menu, Dish
from menu.views import param_replace


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

    def test_user_not_logged_in(self):
        url = reverse('create_menu')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

        url = reverse('add_dish_to_menu', args=['0'])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

        url = reverse('menu_detail', args=['0'])
        response = self.client.post(url, {'dish_id': '4'})
        self.assertEquals(response.status_code, 403)

        url = reverse('edit_menu', args=['0'])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

        url = reverse('edit_dish', args=['0'])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

        url = reverse('delete_menu', args=['0'])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

        url = reverse('delete_dish', args=['0'])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_view_not_empty_menu_shows(self):
        queryset = Menu.objects.get(pk=30)
        queryset.dishes.add('1')
        queryset.save()

        queryset = Menu.objects.get(pk=15)
        queryset.dishes.add('1')
        queryset.save()

        queryset = Menu.objects.filter(dishes_count__gt=0)

        url = reverse('home')
        response = self.client.get(url)

        for q in queryset:
            self.assertContains(response, q.name)

    def test_home_view_pagination(self):
        url = reverse('home')
        self.client.login(username='testuser1', password='abcd')

        response = self.client.get(url)
        for i in range(10):
            self.assertContains(response, f'menu {i}')

        response = self.client.get(url + '?page=2')
        for i in range(10, 20):
            self.assertContains(response, f'menu {i}')

    def test_dish_list_view(self):
        url = reverse('dish_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_dish_list_view_pagination(self):
        url = reverse('dish_list')
        self.client.login(username='testuser1', password='abcd')

        response = self.client.get(url)
        for i in range(10):
            self.assertContains(response, f'danie {i}')

        response = self.client.get(url + '?page=2')
        for i in range(10, 20):
            self.assertContains(response, f'danie {i}')

    def test_home_view_searching(self):
        url = reverse('home')
        self.client.login(username='testuser1', password='abcd')

        response = self.client.get(url + '?name=24')
        self.assertContains(response, 'menu 24')

        response = self.client.get(url + '?name=24')
        self.assertContains(response, 'menu 24')

        response = self.client.get(url + '?sorting=name&sorting_direction=ASC')
        self.assertContains(response, 'menu 1')

        response = self.client.get(url + '?sorting=name&sorting_direction=DESC')
        self.assertContains(response, 'menu 49')

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

    def test_create_menu_view(self):
        self.client.login(username='testuser1', password='abcd')
        url = reverse('create_menu')
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

    def test_create_dish_view(self):
        self.client.login(username='testuser1', password='abcd')
        url = reverse('create_dish')
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

    def test_create_dish_view(self):
        self.client.login(username='testuser1', password='abcd')
        url = reverse('create_dish')
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

    def test_add_dish_to_menu_view(self):
        self.client.login(username='testuser1', password='abcd')
        url = reverse('add_dish_to_menu', args=[self.menu_queryset[0].pk])
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

    def test_adding_dish_to_menu_view(self):
        test_menu = Menu()
        test_menu.name = 'Test menu'
        test_menu.description = 'Test description'
        test_menu.save()

        test_menu_queryset = Menu.objects.get(pk=test_menu.pk)

        self.client.login(username='testuser1', password='abcd')
        url = reverse('add_dish_to_menu', args=[test_menu_queryset.pk])
        response = self.client.post(url, {'dish_pk': '5'})

        test_menu_queryset = Menu.objects.get(pk=test_menu.pk)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(test_menu_queryset.dishes_count, 1)
        self.assertEquals(test_menu_queryset.dishes.count(), 1)

    def test_remove_dish_from_menu(self):
        self.client.login(username='testuser1', password='abcd')
        url = reverse('menu_detail', args=[self.menu_queryset[0].pk])
        response = self.client.post(url, {'dish_pk': str(self.dish_queryset[5].pk)})

        self.assertEquals(response.status_code, 302)