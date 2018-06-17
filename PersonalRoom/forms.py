from django import forms

from .models import *


class FormAdditionalUser(forms.ModelForm):
    class Meta:
        model = AdditionalUser
        exclude = ['user']
