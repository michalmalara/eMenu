from django.test import SimpleTestCase
from django.urls import resolve, reverse

from menu.views import MenuListView, MenuDetailView, DishDetailView, MenuCreateView, DishCreateView, AddDishToMenu, \
    DishListView, MenuUpdateView, DishUpdateView, MenuDeleteView, DishDeleteView
from django.contrib.auth import views as auth_views


class TestUrls(SimpleTestCase):
    def test_login_url_is_ok(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.__name__, auth_views.LoginView.as_view().__name__)
        self.assertTemplateUsed('registration/login.html')

    def test_logout_url_is_ok(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.__name__, auth_views.LogoutView.as_view().__name__)
        self.assertTemplateUsed('registration/logout.html')

    def test_home_url_is_ok(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.__name__, MenuListView.as_view().__name__)
        self.assertTemplateUsed('index.html')

    def test_menu_detail_url_is_ok(self):
        url = reverse('menu_detail', args=[0])
        self.assertEquals(resolve(url).func.__name__, MenuDetailView.as_view().__name__)
        self.assertTemplateUsed('menu_detail_view.html')

    def test_dish_list_url_is_ok(self):
        url = reverse('dish_list')
        self.assertEquals(resolve(url).func.__name__, DishListView.as_view().__name__)
        self.assertTemplateUsed('dish_list_view.html')

    def test_dish_detail_url_is_ok(self):
        url = reverse('dish_detail', args=[0])
        self.assertEquals(resolve(url).func.__name__, DishDetailView.as_view().__name__)
        self.assertTemplateUsed('dish_detail_view.html')

    def test_create_menu_url_is_ok(self):
        url = reverse('create_menu')
        self.assertEquals(resolve(url).func.__name__, MenuCreateView.as_view().__name__)
        self.assertTemplateUsed('create_menu_view.html')

    def test_create_dish_url_is_ok(self):
        url = reverse('create_dish')
        self.assertEquals(resolve(url).func.__name__, DishCreateView.as_view().__name__)
        self.assertTemplateUsed('create_dish_view.html')

    def test_add_dish_to_menu_url_is_ok(self):
        url = reverse('add_dish_to_menu', args=[0])
        self.assertEquals(resolve(url).func.__name__, AddDishToMenu.as_view().__name__)
        self.assertTemplateUsed('add_dish_to_menu.html')

    def test_edit_menu_url_is_ok(self):
        url = reverse('edit_menu', args=[0])
        self.assertEquals(resolve(url).func.__name__, MenuUpdateView.as_view().__name__)
        self.assertTemplateUsed('edit_menu_view.html')

    def test_edit_dish_url_is_ok(self):
        url = reverse('edit_dish', args=[0])
        self.assertEquals(resolve(url).func.__name__, DishUpdateView.as_view().__name__)
        self.assertTemplateUsed('edit_dish_view.html')

    def test_delete_menu_url_is_ok(self):
        url = reverse('delete_menu', args=[0])
        self.assertEquals(resolve(url).func.__name__, MenuDeleteView.as_view().__name__)
        self.assertTemplateUsed('menu_delete_confirmation.html')

    def test_delete_dish_url_is_ok(self):
        url = reverse('delete_dish', args=[0])
        self.assertEquals(resolve(url).func.__name__, DishDeleteView.as_view().__name__)
        self.assertTemplateUsed('dish_delete_confirmation.html')