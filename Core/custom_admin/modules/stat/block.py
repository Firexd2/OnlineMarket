from admin_tools.dashboard import modules
from Orders.models import *


class StatOrderModule(modules.DashboardModule):
    order = Order.objects
    title = u'Заказы'

    def is_empty(self):
        return False

    def __init__(self, **kwargs):
        super(StatOrderModule, self).__init__(**kwargs)
        self.template = 'modules_for_admin/stat/order.html'
        self.all = self.order.all().count()
        self.new = self.order.filter(status='processed').count()
        self.road = self.order.filter(status='road').count()
        self.success = self.order.filter(status='delivered').count()


# class StatVisitedModule(modules.DashboardModule):
#     title = u'Посещения'
#
#     def is_empty(self):
#         return False
#
#     def __init__(self, **kwargs):
#         super(StatVisitedModule, self).__init__(**kwargs)
#         self.template = 'modules_for_admin/stat/visited.html'

