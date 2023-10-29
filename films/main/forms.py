from django import forms
from .models import *

class Search_vid(forms.Form):
    name = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'class': 'fake-editable'}))
    