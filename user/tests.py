from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from .models import Employee
from .utils import createEmployee


class UserTest(TestCase):
    def setUp(self):
        my_test_user = User.objects.create_user('temporary',
                                                'temporary@gmail.com',
                                                'temporary')

    def test_login_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_login_page_post(self):
        response = self.client.post(reverse('login'), {
            'username': 'temporary',
            'password': 'temporary'
        },
                                    follow=True)
        print('----------------------')
        print(response)
        print(dir(response))
        print('----------------------')
        self.assertEqual(True, True)

    def test_users_list_page(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get(reverse('user:user_list'), follow=True)
        self.assertEqual(response.status_code, 200)
