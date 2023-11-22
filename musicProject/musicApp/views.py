from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import *
from .forms import *


def index(request):
    return redirect('songs')


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


class loginView(FormView):
    form_class = loginForm
    template_name = "musicApp/login.html"
    success_url = "/"

    def form_valid(self, form):
        user = form.login()
        if user:
            return redirect('home')
        else:
            return self.form_invalid(form)


class registerView(FormView):
    form_class = registerForm
    template_name = "musicApp/register.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class aboutView(TemplateView):
    template_name = "musicApp/about.html"