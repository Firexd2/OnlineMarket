from django.conf.urls import url
from django.contrib.auth.models import User
from django.urls import path
from AdminPanel.forms import OrderForm
from Baskets.models import ElementBasket
from Orders.models import Order
from Products.models import Product
from .views import *


urlpatterns = [
    url(r'^$', AdminPanelView.as_view()),
    url(r'orders/$', ListAdminView.as_view(model=Order, title='Все заказы')),
    url(r'orders_processed/$', ListAdminView.as_view(model=Order,
                                                     title='Новые заказы', filter={'status': 'processed'})),
    url(r'basket/$', ListAdminView.as_view(template_name='table/basket.html',
                                           model=ElementBasket, title='Элементы корзины')),
    url(r'products/$', ListAdminView.as_view(template_name='table/products.html', model=Product, title='Список продуктов')),
    url(r'users/$', ListAdminView.as_view(template_name='table/user.html',
                                          model=User, title='Зарегистрированные пользователи')),
    path(r'detail_order/<int:pk>/', DetailObjectAdmin.as_view(model=Order, title='Детализация заказа',
                                                              template_name='detail/order.html'), name='detail_order'),

    path(r'detail_product/<int:pk>/', DetailObjectAdmin.as_view(model=Product, title='Детализация продукта',
                                                                template_name='detail/product.html'), name='detail_product_admin'),



    path(r'update_order/<int:pk>/', UpdateObjectAdmin.as_view(model=Order, form_class=OrderForm), name='update_order')
]