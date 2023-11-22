from django import forms
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import *

class songForm(forms.ModelForm):
    class Meta:
        model = song
        fields = ['name', 'artist', 'description']

class registerForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = ["name", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 == password2:
            user.set_password(password1)
            if commit:
                user.save()
                # Log in the user
                user = authenticate(username=user.username, password=password1)
                login(self.request, user)
                # Redirect to the home page
                return redirect('home')
        else:
            raise forms.ValidationError("Passwords do not match.")
            
class loginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(name=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid username or password.")
        return cleaned_data
