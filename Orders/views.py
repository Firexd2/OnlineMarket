from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from Baskets.models import ElementBasket
from Orders.forms import *
from PersonalRoom.models import AdditionalUser, get_or_none


def order(request):

    additional_user_or_none = get_or_none(AdditionalUser, user=request.user.id)
    additional_user = model_to_dict(additional_user_or_none) if additional_user_or_none else None

    form_order = OrderForm(request.POST or None, initial=additional_user)

    if request.user.is_authenticated:
        products = ElementBasket.objects.filter(user=request.user.id)
    else:
        products = ElementBasket.objects.filter(session_id=request.session.session_key)

    if request.POST:
        if form_order.is_valid() and products.count() > 0:
            _order = form_order.save(commit=False)
            if request.user.is_authenticated:
                _order.username = request.user.username
            _order.save()
            for item in products:
                order_product = OrderItemProduct(product=item.product, count=item.count)
                order_product.save()
                _order.products.add(order_product)
            products.delete()
            return render(request, 'order_success.html', locals())

    return render(request, 'order.html', locals())


def repeat_order(request, id):

    order = Order.objects.get(id=id)
    form_order = OrderForm(request.POST or None, initial=model_to_dict(order))
    products = order.products.all()

    if request.is_ajax():
        logistic = order.logistic
        payment = order.payment
        data = {'logistic': logistic, 'payment': payment}
        return JsonResponse(data)

    if request.POST:
        if form_order.is_valid():
            order = form_order.save(commit=False)
            order.status = 'processed'
            order.username = request.user.username
            order.save()
        for item in products:
            order.products.add(item)
        return render(request, 'order_success.html', locals())

    return render(request, 'order.html', locals())


def remove_order(request):
    if request.is_ajax():
        Order.objects.get(id=request.POST['id']).delete()
    return HttpResponse('ok')