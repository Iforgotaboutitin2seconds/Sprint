from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import get_user_model
from django.contrib import messages

def index(request):
    return redirect('songs')

class songListView(ListView):
    model = song
    context_object_name = "songs"
    template_name = "musicApp/song_list.html"


class songDetailView(DetailView):
    model = song
    template_name = "musicApp/song_detail.html"


class playlistListView(ListView):
    model = playlist
    template_name = "musicApp/playlist_list.html"


class playlistDetailView(DetailView):
    model = playlist
    template_name = "musicApp/playlist_detail.html"


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
    success_url = "/songs/"

    def form_valid(self, form):
        user = form.user
        if user:
            login(self.request, user)  # Log in the user
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        # Handle form errors
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)


class registerView(FormView):
    model = get_user_model
    form_class = registerForm
    template_name = "musicApp/register.html"
    success_url = "/songs/"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponse("You are already logged in.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = get_user_model().objects.create_user(name=name,email=email, password=password)
        login(self.request, user)
        return redirect('/')

    def form_invalid(self, form):
        # Handle form errors
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)


class aboutView(TemplateView):
    template_name = "musicApp/about.html"
