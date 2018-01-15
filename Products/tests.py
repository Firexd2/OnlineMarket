from django.test import TestCase
from Products.models import Product, SettingsProduct, Category


class ProductTest(TestCase):

    def setUp(self):
        # Создание характеристики продукта
        SettingsProduct(proteins='10 г.', fats='302 г.', net_weight='500 г').save()
        # Создаем категории
        cat_1 = Category(name='Яблоко')
        cat_1.save()
        cat_2 = Category(name='Хит продаж')
        cat_2.save()
        cat_3 = Category(name='Новинки')
        cat_3.save()
        # Создаем продукт
        product = Product(name='Антоновка', price=100, weight=30, settings_id='1', number=20)
        product.save()
        product.category.add(cat_1, cat_2, cat_3)

    def test_settings_products(self):
        # Для проверки функции создаем экземпляр
        settings = SettingsProduct.objects.get(id='1')
        # Создаем список verbose_name полей, которые должны быть
        VERBOSE_NAMES = ['Белки', 'Жиры', 'Углеводы', 'Калорийность', 'Вес нетто', 'Упаковка',
                         'Срок хранения', 'Производитель', 'Страна производитель', 'Торговая марка']
        value = 0
        verbose = 0
        # Функция all выводит в список verbose_name и value
        for item in settings.all():
            # В экземпляре мы добавили только 3 записи, остальное None
            if item[1]:
                value += 1
            if item[0] in VERBOSE_NAMES:
                verbose += 1

        self.assertEqual(value, 3)
        self.assertEqual(verbose, 10)

    def test_name_url_category(self):
        self.assertEqual(Category.objects.get(id='1').name_url, 'yabloko')

    def test_name_url_product(self):
        self.assertEqual(Product.objects.get(id='1').name_url, 'antonovka')

    def test_sail_procent_product(self):
        product = Product.objects.get(id='1')
        self.assertEqual(bool(product.new_price), bool(product.sail_procent))

    def test_availability_product(self):
        product = Product.objects.get(id='1')
        self.assertEqual(bool(product.number), bool(product.availability))

    def test_icon_value_product(self):
        product = Product.objects.get(id='1')
        # Метод icon_value помогает отображать спец. значки на продукте
        self.assertEqual(product.icon_value(), '01' or '10')

    def test_detail_product(self):
        response = self.client.get('/product/antonovka/')
        self.assertEqual(response.status_code, 200)

    def test_category_detail(self):
        response = self.client.get('/catalog/yabloko/')
        self.assertEqual(response.status_code, 200)

    def test_category_list(self):
        response = self.client.get('/catalog/')
        self.assertEqual(response.status_code, 200)
