from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(song)
admin.site.register(playlist)
admin.site.register(artist)
admin.site.register(user)