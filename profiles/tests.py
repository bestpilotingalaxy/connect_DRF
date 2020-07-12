from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from django.urls import reverse


class AuthTestCase(APITestCase):
    def test_profiles_list(self):
        url = reverse('profile')
        response = self.client.get(url)
        print(response)
