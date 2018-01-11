from django.contrib import admin
from Orders.models import *
from Core.admin import admin_panel, MixinSearchElements

admin.site.register(Order, MixinSearchElements)

admin.site.register(OrderItemProduct, MixinSearchElements)

admin_panel.register(Order, MixinSearchElements)

admin_panel.register(OrderItemProduct, MixinSearchElements)
