from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import get_user_model

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
    success_url = "/songs/"

    def form_valid(self, form):
        user = form.user
        if user:
            login(self.request, user)  # Log in the user
            return redirect('/')
        else:
            return self.form_invalid(form)


class registerView(FormView):
    model = get_user_model
    form_class = registerForm
    template_name = "musicApp/register.html"
    success_url = "/songs/"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponse("You are already logged in.")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = get_user_model().objects.create_user(name=name,email=email, password=password)
            login(request, user)
            return redirect('/')
        else:
            return self.form_invalid(form)


class aboutView(TemplateView):
    template_name = "musicApp/about.html"