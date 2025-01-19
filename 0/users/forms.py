from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'mobile')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')