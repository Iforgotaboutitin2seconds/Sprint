from django.shortcuts import render
from django.views.generic import *
from django.http import HttpResponse
from .models import *

class songListView(ListView):
    model = song

class songDetailView(DetailView):
    model = song

class playListListView(ListView):
    model = playList

class playListDetailView(DetailView):
    model = playList