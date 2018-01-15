from django.shortcuts import render
from Products.models import *


def home(request):
    # Для экономии запросов к БД номера категорий вписываются в ручную
    hit = 8
    new = 1
    products = Product.objects.filter(category__in=[hit, new])[:10]
    return render(request, 'home.html', locals())
