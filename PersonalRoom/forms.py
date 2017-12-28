from django import forms
from django.forms import TextInput

from .models import *

class FormAdditionalUser(forms.ModelForm):

    class Meta:
        model = AdditionalUser
        exclude = ['user']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control', 'id': 'phone-order'}),
            'city': TextInput(attrs={'class': 'form-control', 'id': 'city'}),
            'street': TextInput(attrs={'class': 'form-control', 'id': 'street'}),
            'house': TextInput(attrs={'class': 'form-control', 'id': 'house'}),
            'building': TextInput(attrs={'class': 'form-control', 'id': 'building'}),
            'flat': TextInput(attrs={'class': 'form-control', 'id': 'flat'}),
        }
