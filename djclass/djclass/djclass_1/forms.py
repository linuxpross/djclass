from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post, PythonModel, webCCC, webgo, webjavascript
from django.contrib.auth.models import AbstractUser


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'video']

class PythonModelForm(forms.ModelForm):
    class Meta:
        model = PythonModel
        fields = ['title_p', 'content_p', 'photo_p', 'video_p']

class WebCCCForm(forms.ModelForm):
    class Meta:
        model = webCCC
        fields = ['title_c', 'content_c', 'photo_c', 'video_c']


class WebgoForm(forms.ModelForm):
    class Meta:
        model = webgo
        fields = ['title_go', 'content_go', 'photo_go', 'video_go']


class WebjavascriptForm(forms.ModelForm):
    class Meta:
        model = webjavascript
        fields = ['title_js', 'content_js', 'photo_js', 'video_js']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']





