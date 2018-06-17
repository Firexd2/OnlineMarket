from django.conf.urls import url
from django.contrib.auth import views as auth_views
from Authentication import views, forms

urlpatterns = [
    url(r'^register/$', views.RegisterFormView.as_view()),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    url(r'^info_send_email/$', views.InfoAfterSendEmail.as_view(), name='info_send_email'),

    url('^login/$', auth_views.login, {'template_name': 'login.html',
                                       'authentication_form': forms.CustomAuthenticationForm}, name='user_login'),

    url(r'^logout/$', auth_views.logout_then_login, {'login_url': '/authentication/login/'}, name='logout'),

    url(r'^password_change/$', auth_views.password_change, {'template_name': 'password_change.html'}),

    url(r'^password_change_done/$', auth_views.password_change_done,
        {'template_name': 'password_change_done.html'}, name='password_change_done'),

    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'password_reset.html'}),

    url(r'^password_reset_done/$', auth_views.password_reset,
        {'template_name': 'password_reset_done.html'}, name='password_reset_done'),

    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm, {'template_name': 'password_change.html'}, name='password_reset_confirm'),

    url(r'^password_reset_complete/$', auth_views.password_reset_complete,
        {'template_name': 'password_reset_complete.html'}, name='password_reset_complete'),
]
