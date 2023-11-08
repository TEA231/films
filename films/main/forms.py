from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Search_vid(forms.Form):
    name = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'class': 'fake-editable'}))

class AddComment(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'add_comment'}))


class Register_form(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form_reg'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form_reg'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form_reg'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2') 