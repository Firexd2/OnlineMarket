from django import forms

from Products import models
from Products.widgets import MultiFileInput


class ImageAdminForm(forms.ModelForm):
    class Meta:
        fields = ['image', 'product']
        model = models.ImageProduct
        widgets = {'image': MultiFileInput}
