from django.contrib.admin import AdminSite
from django.contrib import admin
from . import models


class AdminPanel(AdminSite):
    pass


admin_panel = AdminPanel(name='admin_panel')


class MixinSearchElements(admin.ModelAdmin):
    pass

    class Media:
        js = ('//ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js',
              '/media/static/admin-search.js', )


admin.site.register(models.Visitation)
