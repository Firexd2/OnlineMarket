from django.http import JsonResponse
from django.shortcuts import render
from Products.models import *


def home(request):
    # Для экономии запросов к БД номера категорий вписываются в ручную
    hit = 8
    new = 1
    products = Product.objects.filter(category__in=[hit, new]).distinct()[:20]
    return render(request, 'home.html', locals())


def search(request):
    products = Product.objects.all()
    data = {}
    if request.POST['input']:
        for n, product in enumerate(products):
            if request.POST['input'] in product.name.lower():
                data[str(n)] = (product.name, product.name_url)
    return JsonResponse(data)
