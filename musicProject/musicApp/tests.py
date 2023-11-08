from django.test import TestCase
from django.urls import reverse
from .models import *
from .views import *

class SongListViewTest(TestCase):
    def setUp(self):
        # Set up any data you need for your tests
        song.objects.create(name='Song 1', artist='Artist 1')
        song.objects.create(name='Song 2', artist='Artist 2')

    def test_song_list_view(self):
        url = reverse('songs')  # Assuming 'song-list' is the URL name for your SongListView
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the expected data from the database
        self.assertContains(response, 'Song 1')
        self.assertContains(response, 'Song 2')
        self.assertContains(response, 'Artist 1')
        self.assertContains(response, 'Artist 2')

class SongDetailViewTest(TestCase):
    def setUp(self):
        # Create a post for testing
        song.objects.create(name='Test Song', description='This is a test song')

    def test_song_detail_view(self):
        response = self.client.get(reverse('songs', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertContains(response, 'Test Post')