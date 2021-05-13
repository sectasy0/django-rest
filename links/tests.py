from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils.timezone import now

from .models import Link
from images.models import User, Plan, UserPlan

from uuid import uuid4

# Create your tests here.
class LinksTests(APITestCase):
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
            
        self.link = Link(expires=(now() + timedelta(seconds=5000)), 
            value=uuid4().hex[:12], protected_data={'test': 'test123'}, user=self.test_user)
        self.link.save()

        self.plan = Plan(plan_name="Enterprise", acces_original=True, expiration_links=True)
        self.plan.save()

        self.user_plan = UserPlan(user=self.test_user, plan=self.plan)
        self.user_plan.save()

    def test_create_link(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_token.key)
        response = self.client.put('/api/v1/shared/', {'expires': 400, 'protected_data': 'test1234'}, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_create_link_too_small(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_token.key)
        response = self.client.put('/api/v1/shared/', {'expires': 200, 'protected_data': 'test1234'}, format='json')
        self.assertEqual(status.HTTP_422_UNPROCESSABLE_ENTITY, response.status_code)

    def test_create_link_too_big(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_token.key)
        response = self.client.put('/api/v1/shared/', {'expires': 50000, 'protected_data': 'test1234'}, format='json')
        self.assertEqual(status.HTTP_422_UNPROCESSABLE_ENTITY, response.status_code)

    def test_create_link_without_data(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_token.key)
        response = self.client.put('/api/v1/shared/', {'expires': 50000}, format='json')
        self.assertEqual(status.HTTP_422_UNPROCESSABLE_ENTITY, response.status_code)

    def test_create_link_without_expires(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_token.key)
        response = self.client.put('/api/v1/shared/', format='json')
        self.assertEqual(status.HTTP_422_UNPROCESSABLE_ENTITY, response.status_code)

    def test_get_links(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_token.key)
        response = self.client.get('/api/v1/shared/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_access_link(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_token.key)
        response = self.client.get(f'/api/v1/shared/{self.link.value}')
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class LinksTests2(APITestCase):
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
            
        self.link = Link(expires=(now() + timedelta(seconds=5000)), 
            value=uuid4().hex[:12], protected_data={'test': 'test123'}, user=self.test_user)
        self.link.save()


    def test_create_link_no_plan(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_token.key)
        response = self.client.put('/api/v1/shared/', {'expires': 400, 'protected_data': 'test1234'}, format='json')
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)


class LinksTests3(APITestCase):
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
            
        self.link = Link(expires=(now() + timedelta(seconds=5000)), 
            value=uuid4().hex[:12], protected_data={'test': 'test123'}, user=self.test_user)
        self.link.save()

        self.plan = Plan(plan_name="Enterprise", acces_original=False, expiration_links=False)
        self.plan.save()

        self.user_plan = UserPlan(user=self.test_user, plan=self.plan)
        self.user_plan.save()


    def test_create_link_no_plan_permissions(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_token.key)
        response = self.client.put('/api/v1/shared/', {'expires': 400, 'protected_data': 'test1234'}, format='json')
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)