from django.test import TestCase, Client
from accounts.models import User

class TestUserAccount(TestCase):
   
    def test_login(self):

        c = Client()

        self.user = User.objects.create_user(
            username= "test",
            password= "test",
        )

        response = c.get('/')

        self.assertEqual(response.status_code, 302)

        c.login(
            username= "test",
            password= "test",
        )

        response = c.get('/')

        self.assertEqual(response.status_code, 200)

        