from django.urls import reverse
from django.db import models
from PIL import Image as Im

_MAX_SIZE = 150
_MAX_SIZE_2 = 500
UPLOAD_IMG_PRODUCTS = 'products/'

class SettingsProduct(models.Model):
    proteins = models.CharField('Белки', max_length=30, blank=True, null=True)
    fats = models.CharField('Жиры', max_length=30, blank=True, null=True)
    carbohydrates = models.CharField('Углеводы', max_length=30, blank=True, null=True)
    caloric_value = models.CharField('Калорийность', max_length=30, blank=True, null=True)
    net_weight = models.CharField('Вес нетто', max_length=30, blank=True, null=True)
    packaging = models.CharField('Упаковка', max_length=30, blank=True, null=True)
    shelf_life = models.CharField('Срок хранения', max_length=30, blank=True, null=True)
    manufacturer = models.CharField('Производитель', max_length=50, blank=True, null=True)
    manufacturer_country = models.CharField('Страна производитель', max_length=50, blank=True, null=True)
    trademark = models.CharField('Торговая марка', max_length=50, blank=True, null=True)
    product_name = models.CharField('Название продукта', max_length=300, blank=True, null=True)

    def __str__(self):
        return self.product_name

    def all(self):
        return [[field.verbose_name, self.__dict__[field.name]] for field in self._meta.get_fields()[2:-1]]


class Category(models.Model):
    name = models.CharField('Название категории', max_length=40)
    name_url = models.CharField('URL категории', max_length=50, default='')

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        dict_letters = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'ye', 'ё': 'yo', 'ж': 'zh', 'з': 'z',
                        'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
                        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', ' ': '_', '-': '_', ',': '_'}
        name_url = ''
        self.name = self.name.lower()
        for letter in self.name:
            try:
                name_url += dict_letters[letter]
            except KeyError:
                name_url += letter
        self.name_url = name_url
        self.name = self.name[0].upper() + self.name[1:]
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_name_url': self.name_url})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField('Название', max_length=300, default='')
    category = models.ManyToManyField(Category, verbose_name='Категория')
    price = models.IntegerField('Цена', default=0)
    new_price = models.IntegerField('Новая цена', blank=True, null=True)
    sail_procent = models.IntegerField('Скидка', blank=True, null=True)
    weight = models.IntegerField('Вес', default=0)
    availability = models.BooleanField('Доступность', default=True)
    sold = models.PositiveIntegerField('Продано', default=0)
    number = models.PositiveIntegerField('Количество в наличии')
    settings = models.ForeignKey(SettingsProduct, verbose_name='Характеристики продукта', on_delete=models.CASCADE)
    description = models.TextField('Описание', default='', blank=True, null=True)
    date = models.DateField('Дата добавления товара', auto_now_add=True)
    name_url = models.CharField('URL', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse('detail_product', kwargs={'name_url': self.name_url})

    def icon_value(self):
        """
        0 - значение NEW
        1 - значение HIT
        """
        category = list(map(lambda x: x[1], self.category.values_list()))
        result = ''
        if 'Новинки' in category:
            result += '0'
        if 'Хит продаж' in category:
            result += '1'

        return result


    def save(self, *args, **kwargs):
        dict_letters = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'ye', 'ё': 'yo', 'ж': 'zh', 'з': 'z',
                        'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
                        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', ' ': '_', '-': '_', ',': '_'}
        name_url = ''
        self.name = self.name.lower()
        for letter in self.name:
            try:
                name_url += dict_letters[letter]
            except KeyError:
                name_url += letter
        self.name_url = name_url
        self.name = self.name[0].upper() + self.name[1:]

        if self.new_price:
            self.sail_procent = 100 - int(self.new_price / self.price * 100)

        if self.number:
            self.availability = True
        else:
            self.availability = False

        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


def directory_path(instance, filename):
    return 'products/{0}/{1}'.format(instance.product.name, filename)

class ImageProduct(models.Model):

    product = models.ForeignKey(Product, verbose_name='К какому товару причастны', on_delete=models.CASCADE)
    image = models.ImageField('Выбери файлы. Можно выбрать несколько', upload_to=directory_path)
    image_resize = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return '%s' % self.product

    def save(self, *args, **kwargs):

        original_image = directory_path(self, self.image).split('.')
        self.image_resize = original_image[0] + '-2.' + original_image[1]

        super(ImageProduct, self).save(*args, **kwargs)

        filename = self.image.path
        width = self.image.width
        height = self.image.height
        max_size = max(width, height)
        image = Im.open(filename)
        image_small = image.resize(
            (round(width / max_size * _MAX_SIZE),
             round(height / max_size * _MAX_SIZE)),
            Im.ANTIALIAS
        )
        filename_2 = filename.split('.')
        img_resize = filename_2[0] + '-2.' + filename_2[1]
        image_small.save(img_resize)
        if max_size > _MAX_SIZE_2:
            image_big = image.resize(
                (round(width / max_size * _MAX_SIZE_2),
                 round(height / max_size * _MAX_SIZE_2)),
                Im.ANTIALIAS
            )
            image_big.save(filename)

    class Meta:
        verbose_name = 'Фотографии товара'
        verbose_name_plural = 'Фотографии товаров'