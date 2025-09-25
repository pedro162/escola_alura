from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            password='admin'
        )

        self.url = reverse('Estudantes-list')

    def test_user_authentication_with_correct_credentials(self):
        """Verify the authentication of a user, informing the correct credentials"""
        user = authenticate(username='admin', password='admin')
        self.assertTrue((user is not None) and user.is_authenticated )

    def test_user_authentication_with_wrong_username(self):
        """Verify the authentication of a user, informing the wrong username"""
        user = authenticate(username='admina', password='admin')
        self.assertFalse((user is not None) and user.is_authenticated )

    def test_user_authentication_with_wrong_password(self):
        """Verify the authentication of a user, informing the wrong password"""
        user = authenticate(username='admin', password='aa')
        self.assertFalse((user is not None) and user.is_authenticated )

    def test_authorized_request(self):
        """Verify an authorized GET request"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_no_authorized_request(self):
        """Verify a not authorized GET request"""
        #self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
