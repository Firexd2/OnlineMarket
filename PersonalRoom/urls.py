from django.conf.urls import url
from PersonalRoom import views

urlpatterns = [
    url(r'^$', views.personal_room, name='personal_room'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^favorites/$', views.favorites, name='favorites'),
    url(r'^add_to_favorites/$', views.add_to_favorites),
    url(r'^remove_to_favorites/$', views.remove_to_favorites),
    ]
