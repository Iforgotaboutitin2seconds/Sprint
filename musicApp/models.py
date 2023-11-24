from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('song_detail', args=[str(self.id)])


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, related_name="playlists")

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
