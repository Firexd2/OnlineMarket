from django.http import JsonResponse

from Baskets.models import ElementBasket
from Products.models import Category
from .models import Visitation


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_info_for_all_page(request):

    # Приветственное сообщение для shop.beloglazov.me
    welcome = False
    if Visitation.objects.filter(ip=get_client_ip(request)):
        welcome = True
    Visitation.objects.update_or_create(ip=get_client_ip(request))

    category_list = Category.objects.all()
    if request.user.is_authenticated:
        basket = ElementBasket.objects.filter(user=request.user.pk)
        number_product_in_basket = sum([item.count for item in basket])
    else:
        week_in_seconds = 604800
        request.session.set_expiry(week_in_seconds*2)
        basket = ElementBasket.objects.filter(session_id=request.session.session_key)
        number_product_in_basket = sum([item.count for item in basket])
    total_amount = 0
    for item in basket:
        price = item.product.new_price if item.product.new_price else item.product.price
        total_amount += price * item.count
    data = {'number_product_in_basket': number_product_in_basket,
            'category_list': category_list, 'total_amount': total_amount, 'welcome': welcome}
    if not request.is_ajax():
        return data
    else:
        del data['category_list']
        del data['welcome']
        return JsonResponse(data)
