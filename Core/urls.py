from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from ProjectOnlineMarket import settings
from Core import views
from Products import views as views_product

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^basket/', include('Baskets.urls')),
    url(r'^order/', include('Orders.urls')),
    url(r'^authentication/', include('Authentication.urls')),
    url(r'^personal_room/', include('PersonalRoom.urls')),
    url(r'^product/', include('Products.urls')),
    url(r'^catalog/$', views_product.category_list, name='category_list'),
    url(r'^catalog/(?P<category_name_url>\w*)/$', views_product.category_detail, name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)