from django.shortcuts import render
from Products.models import *


def home(request):
    products_list = Product.objects.all().order_by('?')[:10]
    return render(request, 'home.html', locals())
