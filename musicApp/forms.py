from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class songForm(forms.ModelForm):
    class Meta:
        model = song
        fields = ['name', 'artist', 'description']


class registerForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = get_user_model()
        fields = ["name", "email", 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        User = get_user_model()
        user = User.objects.filter(email=email).first()
        if user:
            raise forms.ValidationError("Email already exists.")

        name = cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Name cannot be empty.")

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

    def save(self):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        return user


class loginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            User = get_user_model()
            user = User.objects.filter(email=email).first()
            if not user or not user.check_password(password):
                raise forms.ValidationError("Invalid email or password.")
            else:
                self.user = user
        return cleaned_data
