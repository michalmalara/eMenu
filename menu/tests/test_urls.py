from django.test import SimpleTestCase
from django.urls import resolve, reverse

from menu.views import MenuListView, MenuDetailView, DishDetailView
from django.contrib.auth import views as auth_views


class TestUrls(SimpleTestCase):
    def test_home_url_is_ok(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.__name__, MenuListView.as_view().__name__)
        self.assertTemplateUsed('index.html')

    def test_menu_detail_url_is_ok(self):
        url = reverse('menu_detail', args=[0])
        self.assertEquals(resolve(url).func.__name__, MenuDetailView.as_view().__name__)
        self.assertTemplateUsed('menu_detail_view.html')

    def test_dish_detail_url_is_ok(self):
        url = reverse('dish_detail', args=[0])
        self.assertEquals(resolve(url).func.__name__, DishDetailView.as_view().__name__)
        self.assertTemplateUsed('dish_detail_view.html')

    def test_login_url_is_ok(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.__name__, auth_views.LoginView.as_view().__name__)
        self.assertTemplateUsed('registration/login.html')

    def test_logout_url_is_ok(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.__name__, auth_views.LogoutView.as_view().__name__)
        self.assertTemplateUsed('registration/logout.html')


