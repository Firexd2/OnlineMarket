from django.contrib.auth.models import User
from django.db import models

from Products.models import Product

class OrderItemProduct(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    count = models.IntegerField('Количество товара')

    def __str__(self):
        return '%s, %s' % (self.product, self.count)

    class Meta:
        verbose_name = 'Элемент заказа (продукты и их количество)'
        verbose_name_plural = 'Элементы заказа (продукты и их количество)'



class Order(models.Model):
    METHODS_LOG = (('mail', 'Почта'), ('courier', 'Курьер'), ('cdek', 'Сдэк'))
    METHODS_PAY = (('cash', 'Наличные'), ('imposed', 'Наложенный'), ('card', 'Карта'), ('non-cash', 'Безналичный'))
    STATUS = (('processed', 'Обрабатывается'), ('preparation', 'Подготовка к отправке'),
              ('road', 'В дороге'), ('delivered', 'Доставлен'))

    first_name = models.CharField('Ваше имя', max_length=100, default='')
    last_name = models.CharField('Ваша фамилия', max_length=100, default='')
    phone = models.CharField('Ваше номер телефона', max_length=16, default='')
    payment = models.CharField('Способ оплаты', max_length=20, choices=METHODS_PAY, default='')
    status = models.CharField(max_length=30, choices=STATUS, default='processed')
    logistic = models.CharField('Доставка', max_length=20, choices=METHODS_LOG, default='')
    city = models.CharField('Город', max_length=100, default='')
    street = models.CharField('Улица', max_length=200, default='')
    house = models.IntegerField('Номер дома')
    building = models.IntegerField('Строение/Владение/Корпус', null=True, blank=True)
    flat = models.IntegerField('Номер квартиры/офиса', null=True, blank=True)
    comment = models.TextField(default='', blank=True)
    products = models.ManyToManyField(OrderItemProduct, verbose_name='Продукты')
    amount_price = models.IntegerField(default=0, blank=True)
    username = models.CharField('Пользователь', max_length=200, default='AnonymousUser')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.last_name, self.phone)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


