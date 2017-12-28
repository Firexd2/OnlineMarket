from django.contrib import admin
from Orders.models import *

admin.site.register(Order)

admin.site.register(OrderItemProduct)