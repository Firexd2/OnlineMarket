from django.conf.urls import url
from Baskets.models import ElementBasket
from Orders.models import Order
from .views import *


urlpatterns = [
    url(r'^$', AdminPanelView.as_view()),
    url(r'orders/$', ListAdminView.as_view(model=Order, title='Все заказы')),
    url(r'orders_processed/$', ListAdminView.as_view(model=Order,
                                                     title='Новые заказы', filter={'status': 'processed'})),
    url(r'basket/$', ListAdminView.as_view(model=ElementBasket, title='Элементы корзины'))
]