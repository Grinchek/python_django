from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post
from tinymce.widgets import TinyMCE

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    image = forms.ImageField(required=False, label="Фото профілю")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'image']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логін", max_length=255)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

    class Meta:
        model = Post
        fields = ['title', 'content']
