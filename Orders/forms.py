from django import forms
from django.forms.widgets import *

from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['status', 'products', 'username']
        widgets = {
            'payment': RadioSelect,
            'logistic': RadioSelect,
            'house': TextInput,
            'building': TextInput,
            'flat': TextInput,
        }
