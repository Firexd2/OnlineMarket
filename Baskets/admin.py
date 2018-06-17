from django.contrib import admin

from Baskets import models
from Core.admin import admin_panel, MixinSearchElements

admin.site.register(models.ElementBasket, MixinSearchElements)
admin_panel.register(models.ElementBasket, MixinSearchElements)
