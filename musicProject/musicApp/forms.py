from django import forms
from .models import song

class songForm(forms.ModelForm):
    class Meta:
        model = song
        fields = ['name', 'artist', 'description']
