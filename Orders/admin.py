from django.contrib import admin

from Core.admin import admin_panel, MixinSearchElements
from Orders.models import *

admin.site.register(Order, MixinSearchElements)

admin.site.register(OrderItemProduct, MixinSearchElements)

admin_panel.register(Order, MixinSearchElements)

admin_panel.register(OrderItemProduct, MixinSearchElements)
