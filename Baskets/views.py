from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from Baskets.models import ElementBasket
from Products.models import Product


def basket_delete(request):
    if request.user.is_authenticated():
        ElementBasket.objects.filter(product=request.POST['id'], user=request.user.id).delete()
    else:
        ElementBasket.objects.filter(product=request.POST['id'], session_id=request.session.session_key).delete()
    return HttpResponse('ok')


def change_count_in_basket(request, product_id):
    if request.user.is_authenticated():
        ElementBasket.objects.filter(product=product_id,
                                     user=request.user.id).update(count=request.POST['count-in-basket'])
    else:
        ElementBasket.objects.filter(product=product_id,
                                     session_id=request.session.session_key).update(count=request.POST['count-in-basket'])
    return HttpResponse('ok')


def basket(request):
    if request.user.is_authenticated():
        elementsBasket = ElementBasket.objects.filter(user=request.user.pk)
    else:
        elementsBasket = ElementBasket.objects.filter(session_id=request.session.session_key)
    return render(request, 'basket.html', locals())


def add_product_in_basket(request):
    if request.user.is_authenticated():
        ElementBasket(product=Product.objects.get(id=request.POST['id']),
                      count=request.POST['count'], user=User.objects.get(id=request.user.pk)).save()
    else:
        ElementBasket(product=Product.objects.get(id=request.POST['id']),
                      count=request.POST['count'], session_id=request.session.session_key).save()
    return HttpResponse('ok')


def get_ids_product_in_basket(request):
    data = {}
    if request.user.is_authenticated():
        list_ids = [item.product.pk for item in ElementBasket.objects.filter(user=request.user.pk)]
    else:
        list_ids = [item.product.pk for item in ElementBasket.objects.filter(session_id=request.session.session_key)]
    for i in list_ids:
        data[i] = ''
    return JsonResponse(data)
