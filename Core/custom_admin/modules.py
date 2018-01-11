from admin_tools.dashboard import modules
from Orders.models import *
from Core.models import Visitation
from Products.models import Product
from datetime import datetime, timedelta


class StatOrderModule(modules.DashboardModule):
    order = Order.objects
    title = u'Заказы'

    def is_empty(self):
        return False

    def filter_status(self, status):
        return self.order.filter(status=status).count()

    def __init__(self, **kwargs):
        super(StatOrderModule, self).__init__(**kwargs)
        self.template = 'modules_for_admin/stat/order.html'
        self.all = self.order.all().count()
        self.new = self.filter_status('processed')
        self.road = self.filter_status('road')
        self.success = self.filter_status('delivered')


class StatVisitedModule(modules.DashboardModule):
    title = u'Посещения'
    visited = Visitation.objects

    def is_empty(self):
        return False

    def visitors_time(self, day):
        return self.visited.filter(date__range=[datetime.today() - timedelta(days=day), datetime.today()]).count()

    def __init__(self, **kwargs):
        super(StatVisitedModule, self).__init__(**kwargs)
        self.template = 'modules_for_admin/stat/visited.html'
        self.all = self.visited.all().count()
        self.today = self.visited.filter(date=datetime.now().date()).count()
        self.week = self.visitors_time(7)
        self.month = self.visitors_time(30)


class StatProductsModule(modules.DashboardModule):
    title = u'Топ-10 продуктов'

    def is_empty(self):
        return False

    def __init__(self, **kwargs):
        super(StatProductsModule, self).__init__(**kwargs)
        self.template = 'modules_for_admin/stat/products.html'
        self.top = Product.objects.all().order_by('-sold')[:10]


class NewOrdersModule(modules.DashboardModule):

    title = u'Новые заказы'

    def is_empty(self):
        return self.orders.count() == 0

    def __init__(self, **kwargs):
        super(NewOrdersModule, self).__init__(**kwargs)
        self.template = 'modules_for_admin/model/orders.html'
        self.orders = Order.objects.filter(status='processed')
        self.count = self.orders.count()
