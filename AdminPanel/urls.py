from django.conf.urls import url
from django.contrib.auth.models import User

from Baskets.models import ElementBasket
from Orders.models import Order
from Products.models import Product
from .views import *


urlpatterns = [
    url(r'^$', AdminPanelView.as_view()),
    url(r'orders/$', ListAdminView.as_view(model=Order, title='Все заказы')),
    url(r'orders_processed/$', ListAdminView.as_view(model=Order,
                                                     title='Новые заказы', filter={'status': 'processed'})),
    url(r'basket/$', ListAdminView.as_view(template_name='admin_basket_table.html',
                                           model=ElementBasket, title='Элементы корзины')),
    url(r'products/$', ListAdminView.as_view(template_name='admin_products_table.html', model=Product, title='Список продуктов')),
    url(r'users/$', ListAdminView.as_view(template_name='admin_user_table.html',
                                          model=User, title='Зарегистрированные пользователи'))
]