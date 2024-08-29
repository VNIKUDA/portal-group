from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.assertEqual(user.username, 'testuser')

