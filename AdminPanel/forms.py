from django import forms

from Orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['']
