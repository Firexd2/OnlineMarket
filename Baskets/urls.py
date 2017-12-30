from django.conf.urls import url
from Baskets import views
from Core import context_processors

urlpatterns = [
    url(r'^$', views.BasketTemplateView.as_view(), name='basket'),
    url(r'^add_product_in_basket$', views.BasketAdd.as_view()),
    url(r'^change_count_in_basket/', views.BasketCount.as_view(), name='change_count_in_basket'),
    url(r'^delete/$', views.BasketDelete.as_view(), name='basket_delete'),
    url(r'^get_data_basket/$', context_processors.category_and_session),
    url(r'^get_ids_product_in_basket/$', views.BasketGet.as_view(), name='get_ids_product_in_basket')
]