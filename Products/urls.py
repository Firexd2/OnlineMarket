from django.conf.urls import url

from Products import views

urlpatterns = [
    url(r'^(?P<name_url>\w*)/$', views.detail_product, name='detail_product'),
]
