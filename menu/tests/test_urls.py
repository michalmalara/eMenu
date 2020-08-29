from django.test import SimpleTestCase
from django.urls import resolve, reverse

from menu.views import firstView


class TestUrls(SimpleTestCase):

    def test_home_url_is_ok(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, firstView)