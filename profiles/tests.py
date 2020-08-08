from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from django.urls import reverse


class AuthTestCase(APITestCase):
    def test_profiles_list(self):
        url = 'http://127.0.0.1:8000/auth/users/'
        data = {
                "email": "ewfwefewff@mail.ru",
                "username": "test_reg_test",
                "password": "kfgntd98"
            }
        response = self.client.post(url, data)
