from django.contrib import admin
from Orders.models import *
from Core.admin import admin_panel, MixinSearchElements

admin.site.register(Order)

admin.site.register(OrderItemProduct)

admin_panel.register(Order, MixinSearchElements)

admin_panel.register(OrderItemProduct, MixinSearchElements)
