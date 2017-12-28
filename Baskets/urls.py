from django.conf.urls import url
from Baskets import views
from Core import context_processors

urlpatterns = [
    url(r'^$', views.basket, name='basket'),
    url(r'^add_product_in_basket$', views.add_product_in_basket),
    url(r'^change_count_in_basket/(?P<product_id>\w+)$', views.change_count_in_basket, name='change_count_in_basket'),
    url(r'^delete/$', views.basket_delete, name='basket_delete'),
    url(r'^get_data_basket/$', context_processors.category_and_session),
    url(r'^get_ids_product_in_basket/$', views.get_ids_product_in_basket, name='get_ids_product_in_basket')
]