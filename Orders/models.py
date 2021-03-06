from django.contrib.auth.models import User
from django.db import models

from Products.models import Product


class OrderItemProduct(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    count = models.IntegerField('Количество')

    def __str__(self):
        return 'Продукт: %s, в количестве: %s шт.' % (self.product, self.count)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    METHODS_LOG = (('mail', 'Почта'), ('courier', 'Курьер'), ('cdek', 'Сдэк'))
    METHODS_PAY = (('cash', 'Наличные'), ('imposed', 'Наложенный'), ('card', 'Карта'), ('non-cash', 'Безналичный'))
    STATUS = (('processed', 'Обрабатывается'), ('preparation', 'Подготовка к отправке'),
              ('road', 'В дороге'), ('delivered', 'Доставлен'))

    first_name = models.CharField('Имя', max_length=100, default='')
    last_name = models.CharField('Фамилия', max_length=100, default='')
    phone = models.CharField('Номер телефона', max_length=16, default='')
    payment = models.CharField('Способ оплаты', max_length=20, choices=METHODS_PAY, default='')
    status = models.CharField('Статус', max_length=30, choices=STATUS, default='processed')
    logistic = models.CharField('Доставка', max_length=20, choices=METHODS_LOG, default='')
    city = models.CharField('Город', max_length=100, default='')
    street = models.CharField('Улица', max_length=200, default='')
    house = models.IntegerField('Номер дома')
    building = models.IntegerField('Строение/Владение/Корпус', null=True, blank=True)
    flat = models.IntegerField('Номер квартиры/офиса', null=True, blank=True)
    comment = models.TextField('Комментарий', default='', blank=True)
    products = models.ManyToManyField(OrderItemProduct, verbose_name='Продукты')
    amount_price = models.IntegerField('Стоимость', default=0, blank=True)
    username = models.CharField('Пользователь', max_length=200, default='AnonymousUser')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '№%s | Имя: %s %s | Телефон: %s | Логин: %s | Дата: %s' % \
               (self.id, self.last_name, self.first_name, self.phone, self.username, self.date.date())

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
