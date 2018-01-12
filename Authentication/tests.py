from django.test import TestCase
from django.test import Client
from Authentication.validator import validate_email_on_unique
from django.core.exceptions import ValidationError
from Authentication.forms import RegistrationForm
from django.contrib.auth.models import User
from .forms import CustomAuthenticationForm as AuthForm
from django.contrib.auth import authenticate


class AuthTest(TestCase):

    def setUp(self):
        user = User(username='test', email='test@gmail.com', is_active=False)
        user.set_password('Qwertyu1234')
        user.save()

    def test_validate_email_on_unique(self):
        """
        Создаем произвольного пользователя и напрямую даём валидатору тот же e-mail
        """
        with self.assertRaises(ValidationError):
            validate_email_on_unique('test@gmail.com')

    def test_login_no_active(self):
        """
        В проекте используется иной бекенд-авторизации, который позволяет авторизовывать no-active users.
        Для отказа авторизации используется валидатор проверки, с выводом сообщения о неактивированном аккаунте.
        """
        client = Client()
        response = client.post('/authentication/login/', {'username': 'test', 'password': 'Qwertyu1234'})

        # авторизация не пройдет с no-active user
        self.assertFalse(response.context['user'].is_authenticated)
