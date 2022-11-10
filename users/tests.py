from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class UserRegistrationTest(APITestCase):
    def test_registration(self): # 모든 test마다 DB를 초기화한다. stateless
        url = reverse("user_view")  # 이름에 해당하는 url
        user_data = {
            "username": "testuser",
            "fullname": "테스터",
            "email": "test@testuser.com",
            "password": "password",
        }
        response = self.client.post(url, user_data)
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        url = reverse("token_obtain_pair")
        user_data = {
            "username": "testuser",
            "fullname": "테스터",
            "email": "test@testuser.com",
            "password": "password",
        }
        response = self.client.post(url, user_data)
        print(response.data)
        self.assertEqual(response.status_code, 200)
