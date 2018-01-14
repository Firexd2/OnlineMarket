from django.test import TestCase, Client
from Baskets.models import ElementBasket
from Products.models import Product, SettingsProduct
from Orders.models import Order, OrderItemProduct
from django.contrib.auth.models import User
from Orders.forms import OrderForm


class OrderCreateTest(TestCase):

    def setUp(self):
        # Создаем юзера
        user = User(username='test', email='test@gmail.com', is_active=True)
        user.set_password('Qwertyu1234')
        user.save()
        # Сохраняем необходимые параметры продукта
        SettingsProduct(proteins='100').save()
        # Сохраняем продукт
        Product(name='TestProduct', number=5, settings_id=1).save()
        # Наполняем корзину
        ElementBasket(product_id='1', user_id='1', count=4).save()

    def test_order(self):

        # Авторизовываем пользователя
        self.client.login(username='test', password='Qwertyu1234')
        # Эмулируем заказ
        response = self.client.post('/order/', {'first_name': 'Денис', 'last_name': 'Белоглазов',
                                'phone': '+7(999)985-34-34', 'city': 'Москва',
                                'street': 'Таганская', 'house': '2', 'flat': '50',
                                'logistic': 'cdek', 'payment': 'card',
                                'comment': 'Test comment for order'})

        # Показывем, что заказ осуществлен
        self.assertTrue(Order.objects.filter(last_name='Белоглазов'))

        # Проверяем, что после заказа был подгружен шаблон 'order_success.html'
        self.assertEqual(response.templates[0].name, 'order_success.html')


class OrderRestTest(TestCase):

    def setUp(self):
        # Создаем юзера
        user = User(username='test', email='test@gmail.com', is_active=True)
        user.set_password('Qwertyu1234')
        user.save()
        # Сохраняем необходимые параметры продукта
        SettingsProduct(proteins='100').save()
        # Сохраняем продукт
        Product(name='TestProduct', number=5, settings_id=1).save()
        # Наполняем корзину
        ElementBasket(product_id='1', user_id='1', count=4).save()
        # Авторизовываем пользователя
        self.client.login(username='test', password='Qwertyu1234')
        # Эмулируем заказ
        self.client.post('/order/', {'first_name': 'Денис', 'last_name': 'Белоглазов',
                                     'phone': '+7(999)985-34-34', 'city': 'Москва',
                                     'street': 'Таганская', 'house': '2', 'flat': '50',
                                     'logistic': 'cdek', 'payment': 'card',
                                     'comment': 'Test comment for order'})

    def test_status_order(self):
        # Статус "processed"
        self.assertEqual(Order.objects.get(pk=1).status, 'processed')

    def test_products_in_order(self):
        # В заказе четыре продукта одной масти
        self.assertEqual(Order.objects.get(pk=1).products.all()[0].count, 4)

    def test_delete_basket_after_order(self):
        # Обнуление корзины
        self.assertFalse(ElementBasket.objects.all().count())

    def test_product_number(self):
        # Проверяем, что количество продукта на складе уменьшилось соответственно:
        self.assertEqual(Product.objects.get(pk=1).number, 5 - 4)

    def test_product_sold(self):
        # Проверяем, что значение проданного продукта увеличилось соответственно:
        self.assertEqual(Product.objects.get(pk=1).sold, 0 + 4)

    def test_remove_order(self):
        # Удаление заказа
        self.client.post('/order/remove/', {'id': '1'})
        self.assertFalse(Order.objects.all())

    def test_repeat_order(self):
        # Повторяем прошлый заказ
        self.client.post('/order/repeat/1/', {'first_name': 'Денис', 'last_name': 'Белоглазов',
                                     'phone': '+7(999)985-34-34', 'city': 'Москва',
                                     'street': 'Таганская', 'house': '2', 'flat': '50',
                                     'logistic': 'cdek', 'payment': 'card',
                                     'comment': 'Test comment for order'})

        self.assertEqual(Order.objects.all().count(), 2)
