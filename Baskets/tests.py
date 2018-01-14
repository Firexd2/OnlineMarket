from django.test import TestCase
from .models import ElementBasket
from Products.models import Product, SettingsProduct
from django.contrib.auth.models import User


class BasketTest(TestCase):

    def setUp(self):
        # Создаем юзера
        user = User(username='test', email='test@gmail.com', is_active=True)
        user.set_password('Qwertyu1234')
        user.save()
        # Сохраняем необходимые параметры продукта
        SettingsProduct(proteins='100').save()
        # Сохраняем продукт
        Product(name='TestProduct', number=5, settings_id=1).save()

    def test_add_basket(self):
        """
        Корзина работает с привязкой к сессии, либо к юзеру. В этом тесте идёт проверка добавления в корзину
        для неавторизованного и авторизованного пользователей.
        """
        # неавторизованный клиент
        self.client.post('/basket/add_product_in_basket', {'id': '1', 'count': '2'})
        self.assertTrue(ElementBasket.objects.get(id=1).user is None)
        # авторизованный клиент
        self.client.login(username='test', password='Qwertyu1234')
        self.client.post('/basket/add_product_in_basket', {'id': '1', 'count': '2'})
        self.assertTrue(ElementBasket.objects.get(id=2).user.is_authenticated)

    def test_delete_basket(self):
        """
        Тест удаления элемента корзины
        """
        self.client.login(username='test', password='Qwertyu1234')
        ElementBasket(product_id=1, count=1, user_id=1).save()
        self.client.post('/basket/delete/', {'id': '1'})
        self.assertTrue(len(ElementBasket.objects.all()) == 0)

    def test_change_count_basket(self):
        """
        Тест изменения количества продуктов в корзине
        """
        self.client.login(username='test', password='Qwertyu1234')
        ElementBasket(product_id=1, count=1, user_id=1).save()
        self.client.post('/basket/change_count_in_basket/', {'id': '1', 'count-in-basket': '9999'})
        self.assertEqual(ElementBasket.objects.get(id=1).count, 9999)

    def test_get_basket(self):
        """
        Тест получения данных о корзине
        """
        self.client.login(username='test', password='Qwertyu1234')
        # Получение данных пустой корзины
        response = self.client.get('/basket/get_ids_product_in_basket/')
        content_before_add_basket = response.content

        ElementBasket(product_id=1, count=1, user_id=1).save()
        # Получение данных не пустой корзины
        response = self.client.get('/basket/get_ids_product_in_basket/')
        content_after_add_basket = response.content
        # Сравниваем возвращаемый контент, представленный строкой
        # В не пустой корзине, строка явно должна быть длиннее
        self.assertTrue(len(content_after_add_basket) > len(content_before_add_basket))
