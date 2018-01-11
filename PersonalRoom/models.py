from django.contrib.auth.models import User
from django.db import models
from Products.models import Product


class AdditionalUser(models.Model):
    first_name = models.CharField('Имя', max_length=100, null=True, blank=True)
    last_name = models.CharField('Фамилия', max_length=100, null=True, blank=True)
    phone = models.CharField('Номер телефона', max_length=16, null=True, blank=True)
    city = models.CharField('Город', max_length=100, null=True, blank=True)
    street = models.CharField('Улица', max_length=200, null=True, blank=True)
    house = models.IntegerField('Номер дома', null=True, blank=True)
    building = models.IntegerField('Строение/Владение/Корпус', null=True, blank=True)
    flat = models.IntegerField('Номер квартиры/офиса', null=True, blank=True)
    user = models.OneToOneField(User, verbose_name='Принадлежность', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'Запись принадлежит: %s' % self.user

    class Meta:
        verbose_name = 'Дополнительная информация о пользователе'
        verbose_name_plural = 'Дополнительная информация о пользователе'


class FavoritesProducts(models.Model):
    products = models.ManyToManyField(Product, verbose_name='Товары')
    user = models.CharField('Пользователь', max_length=100)

    def __str__(self):
        return 'Продукты %s у %s' % (self.products.all(), self.user)

    class Meta:
        verbose_name = 'Избранный товар'
        verbose_name_plural = 'Избранные товары'


def get_or_none(self, **kwargs):
    try:
        return self.objects.get(**kwargs).products.all()
    except self.DoesNotExist:
        return None
