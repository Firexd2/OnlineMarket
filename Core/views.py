from django.http import JsonResponse
from django.shortcuts import render

from Core.models import SlideBanner
from Products.models import *


def home(request):
    hit = 'Новинки'
    new = 'Хит продаж'
    products = Product.objects.filter(category__name__in=[hit, new]).distinct()[:20]
    slides = SlideBanner.objects.all()[::-1]
    return render(request, 'home.html', locals())


def search(request):
    products = Product.objects.all()
    data = {}
    if request.POST['input']:
        for n, product in enumerate(products):
            if request.POST['input'] in product.name.lower():
                data[str(n)] = (product.name, product.name_url)
    return JsonResponse(data)
