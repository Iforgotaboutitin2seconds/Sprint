from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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

class UserManager(BaseUserManager):
    def create_user(self, email, name, password):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

class user(AbstractBaseUser):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)  # Add this line

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True