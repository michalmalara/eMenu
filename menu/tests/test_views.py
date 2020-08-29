from django.test import TestCase
from django.test import Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homeUrl = reverse('home')

    def test_home_view(self):
        response = self.client.get(self.homeUrl)

        self.assertEquals(response.status_code, 200)


