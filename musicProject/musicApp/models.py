from django.db import models
from django.urls import reverse


class song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('song_detail', args=[str(self.id)])


class playlist(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    songs = models.ManyToManyField(song, related_name="playlists")

    def __str__(self):
        return self.name

class user(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    playlists = models.ManyToManyField(playlist, related_name="users")

    def __str__(self):
        return self.name
