from django.test import TestCase, Client
from django.urls import reverse
from .models import Song, Playlist, User
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class URLTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(email='test@test.com', name='test', password='testpass')
        self.client.login(email='test@test.com', password='testpass')

    def test_songs_url(self):
        response = self.client.get(reverse('songs'))
        self.assertEqual(response.status_code, 200)

    def test_about_url(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)


class ModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', name='test', password='testpass')

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
        self.assertEqual(self.user.name, 'test')

    def test_song_creation(self):
        self.assertEqual(self.song.name, 'Test Song')
        self.assertEqual(self.song.artist, 'Test Artist')
        self.assertEqual(self.song.description, 'Test Description')

    def test_playlist_creation(self):
        self.assertEqual(self.playlist.name, 'Test Playlist')
        self.assertEqual(self.playlist.artist, 'Test Artist')
        self.assertIn(self.song, self.playlist.songs.all())

class SeleniumTest(StaticLiveServerTestCase):

    def test_links(self):
        # Open the web browser and go to the live server
        self.driver = driver = webdriver.Chrome()
        driver.get(self.live_server_url)

        # Check if the title is correct
        title = driver.title
        assert title == "Music App"
        self.driver.implicitly_wait(10)

        # Check if the Songs link is present
        songs_link = self.driver.find_element(By.LINK_TEXT, 'Songs')
        self.assertIsNotNone(songs_link)

        # Check if the About link is present
        about_link = self.driver.find_element(By.LINK_TEXT, 'About')
        self.assertIsNotNone(about_link)

        # Check if the Login link is present
        login_link = self.driver.find_element(By.LINK_TEXT, 'Login')
        self.assertIsNotNone(login_link)
        
        self.driver.quit()
