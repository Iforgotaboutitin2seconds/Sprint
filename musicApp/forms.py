from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.auth import authenticate

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'artist', 'description']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = get_user_model()
        fields = ["email", 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        user = get_user_model().objects.filter(email=email).first()
        if user:
            raise forms.ValidationError("Email already exists.")

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

    def save(self):
        user = super().save(commit=False)
        user.save()
        return user


class LoginForm(AuthenticationForm):
    pass