from django.conf.urls import url

from Orders import views

urlpatterns = [
    url(r'^$', views.order, name='order'),
    url(r'repeat/(?P<id>\w*)/$', views.repeat_order, name='repeat-order'),
    url(r'remove/$', views.remove_order, name='remove-order')
]
