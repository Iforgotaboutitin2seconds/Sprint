from django.test import TestCase, Client
from django.urls import reverse

class URLTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_url(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_songs_url(self):
        response = self.client.get(reverse('songs'))
        self.assertEqual(response.status_code, 200)

    def test_about_url(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)