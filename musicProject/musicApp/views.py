from django.shortcuts import render
from django.views.generic import *
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import songForm


def index(request):
    return render(request, "musicApp/song_list.html")


class songListView(ListView):
    model = song
    context_object_name = "songs"


class songDetailView(DetailView):
    model = song


class playlistListView(ListView):
    model = playlist


class playlistDetailView(DetailView):
    model = playlist


class songCreateView(LoginRequiredMixin, CreateView):
    model = song
    form_class = songForm
    template_name = "musicApp/song_form.html"


class songUpdateView(LoginRequiredMixin, UpdateView):
    model = song
    form_class = songForm
    template_name = "musicApp/song_form.html"


class songDeleteView(LoginRequiredMixin, DeleteView):
    model = song
    template_name = "musicApp/song_confirm_delete.html"
    success_url = "/songs/"

class loginView(TemplateView):
    template_name = "musicApp/login.html"

class registerView(TemplateView):
    model = user
    template_name = "musicApp/register.html"