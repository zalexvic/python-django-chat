from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    handle = forms.CharField()
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'handle', 'password1', 'password2', 'profile_pic']