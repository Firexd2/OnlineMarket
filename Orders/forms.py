from django import forms
from django.forms.widgets import *
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['status', 'products', 'username']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control', 'id': 'phone-order'}),
            'city': TextInput(attrs={'class': 'form-control', 'id': 'city'}),
            'street': TextInput(attrs={'class': 'form-control', 'id': 'street'}),
            'house': TextInput(attrs={'class': 'form-control', 'id': 'house'}),
            'building': TextInput(attrs={'class': 'form-control', 'id': 'building'}),
            'flat': TextInput(attrs={'class': 'form-control', 'id': 'flat'}),
            'payment': RadioSelect,
            'logistic': RadioSelect,
            'comment': Textarea(attrs={'class': 'form-control textarea-order', 'rows': '5'})
        }
