from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from PIL import Image

import tempfile
import io

# Create your tests here.
class ImageTests(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            first_name="Test",
            last_name="User",
            username="testuser",
            email="test@user.com",
            is_active=True,
            is_staff=False)
        self.test_user.set_password('demo1234')
        self.test_user.save()
        self.test_user_token, created = Token.objects.get_or_create(
            user=self.test_user)

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_upload_image(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_token.key)
        response = self.client.put('/api/v1/image/upload/', {'file': self.generate_photo_file(), 'format': 'png'}, format='multipart')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_upload_image_without_format(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_token.key)
        response = self.client.put('/api/v1/image/upload/', {'file': self.generate_photo_file()}, format='multipart')
        self.assertEqual(status.HTTP_422_UNPROCESSABLE_ENTITY, response.status_code)

    def test_upload_without_image_and_format(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_token.key)
        response = self.client.put('/api/v1/image/upload/', format='multipart')
        self.assertEqual(status.HTTP_422_UNPROCESSABLE_ENTITY, response.status_code)

    def test_get_images(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_token.key)
        response = self.client.get('/api/v1/images/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)


