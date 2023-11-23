from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Song, Playlist

class URLTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_songs_url(self):
        response = self.client.get(reverse('songs'))
        self.assertEqual(response.status_code, 200)

    def test_about_url(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)


class ModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', username='test', password='testpass')

        self.song = Song.objects.create(
            name='Test Song',
            artist='Test Artist',
            description='Test Description'
        )

        self.playlist = Playlist.objects.create(
            name='Test Playlist',
            artist='Test Artist'
        )
        self.playlist.songs.add(self.song)

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@test.com')
        self.assertEqual(self.user.username, 'test')

    def test_song_creation(self):
        self.assertEqual(self.song.name, 'Test Song')
        self.assertEqual(self.song.artist, 'Test Artist')
        self.assertEqual(self.song.description, 'Test Description')

    def test_playlist_creation(self):
        self.assertEqual(self.playlist.name, 'Test Playlist')
        self.assertEqual(self.playlist.artist, 'Test Artist')
        self.assertIn(self.song, self.playlist.songs.all())