from django.test import TestCase
from .urls import urlpatterns
from django.contrib.auth.models import User
from PersonalRoom.models import AdditionalUser, FavoritesProducts
from Products.models import Product, SettingsProduct


class PersonalRoomTest(TestCase):

    def setUp(self):
        # Создаем юзера
        user = User(username='test', email='test@gmail.com', is_active=True)
        user.set_password('Qwertyu1234')
        user.save()

    def test_status_code_personal_room(self):
        # Не авторизованный пользователь
        response = self.client.get('/personal_room/')
        # Код редиректа
        self.assertEqual(response.status_code, 302)
        # Авторизованный пользователь
        self.client.login(username='test', password='Qwertyu1234')
        response = self.client.get('/personal_room/')
        self.assertEqual(response.status_code, 200)

    def test_status_code_favorites(self):
        # Не авторизованный пользователь
        response = self.client.get('/personal_room/favorites/')
        # Код редиректа
        self.assertEqual(response.status_code, 302)
        # Авторизованный пользователь
        self.client.login(username='test', password='Qwertyu1234')
        response = self.client.get('/personal_room/favorites/')
        self.assertEqual(response.status_code, 200)

    def test_save_additional_user(self):
        self.client.login(username='test', password='Qwertyu1234')
        # Эмулируем пользовательский ввод дополнительных данных
        self.client.post('/personal_room/profile/', {'last_name': 'Белоглазов', 'city': 'Москва'})
        # Проверяем соответствующую созданную запись
        self.assertTrue(AdditionalUser.objects.filter(user_id='1'))

    def test_favorites_actions(self):
        self.client.login(username='test', password='Qwertyu1234')
        # Сохраняем необходимые параметры продукта
        SettingsProduct(proteins='100').save()
        # Сохраняем продукт
        Product(name='Testproduct', number=5, settings_id=1).save()
        # Добавляем в избранное
        self.client.post('/personal_room/add_to_favorites/', {'id': '1'})
        self.assertEqual(FavoritesProducts.objects.get(user='test').products.all()[0].name, 'Testproduct')
        # Удаляем из избранного
        self.client.post('/personal_room/remove_to_favorites/', {'id': '1'})
        self.assertFalse(FavoritesProducts.objects.get(user='test').products.all())
