from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from Baskets.models import ElementBasket
from Orders.forms import *
from PersonalRoom.models import AdditionalUser


def order(request):

    try:
        additional_user = model_to_dict(AdditionalUser.objects.get(user=request.user.id))
    except ObjectDoesNotExist:
        additional_user = None

    form_order = OrderForm(request.POST or None, initial=additional_user)

    if request.user.is_authenticated:
        products = ElementBasket.objects.filter(user=request.user.id)
    else:
        products = ElementBasket.objects.filter(session_id=request.session.session_key)

    if request.POST:
        if form_order.is_valid() and products.count() > 0:
            save_order = form_order.save(commit=False)
            if request.user.is_authenticated:
                save_order.username = request.user.username
            save_order.save()
            for item in products:
                order_product = OrderItemProduct(product=item.product, count=item.count)
                order_product.save()
                save_order.products.add(order_product)
                product = item.product
                product.number -= item.count
                product.sold += item.count
                product.save()

            products.delete()
            return render(request, 'order_success.html', locals())

    return render(request, 'order.html', locals())


def repeat_order(request, id):
    save_order = None
    _order = Order.objects.get(id=id)
    form_order = OrderForm(request.POST or None, initial=model_to_dict(_order))
    products = _order.products.all()

    if request.is_ajax():
        logistic = _order.logistic
        payment = _order.payment
        data = {'logistic': logistic, 'payment': payment}
        return JsonResponse(data)

    if request.POST:
        if form_order.is_valid():
            save_order = form_order.save(commit=False)
            save_order.status = 'processed'
            save_order.username = request.user.username
            save_order.save()
        for item in products:
            save_order.products.add(item)
        return render(request, 'order_success.html', locals())

    return render(request, 'order.html', locals())


def remove_order(request):
    if request.POST:
        Order.objects.get(id=request.POST['id']).delete()
    return HttpResponse('ok')
