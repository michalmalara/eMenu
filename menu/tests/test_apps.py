from django.apps import apps
from django.test import TestCase
from menu.apps import MenuConfig


class ReportsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(MenuConfig.name, 'menu')
        self.assertEqual(apps.get_app_config('menu').name, 'menu')