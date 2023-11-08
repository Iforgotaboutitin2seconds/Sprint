from django.shortcuts import render
from django.views.generic import *
from django.http import HttpResponse
from .models import *
from .forms import songForm

def index(request):
    return render(request, 'musicApp/song_list.html')

class songListView(ListView):
    model = song
    context_object_name = 'songs'

class songDetailView(DetailView):
    model = song

class playListListView(ListView):
    model = playList

class playListDetailView(DetailView):
    model = playList


class songCreateView(CreateView):
    model = song
    form_class = songForm
    template_name = 'musicApp/song_form.html'

class songUpdateView(UpdateView):
    model = song
    form_class = songForm
    template_name = 'musicApp/song_form.html'

class songDeleteView(DeleteView):
    model = song
    template_name = 'musicApp/song_confirm_delete.html'
    success_url = '/songs/'