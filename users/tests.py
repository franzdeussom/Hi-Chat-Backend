from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from users.models import User


class TestUser(APITestCase):
    url = reverse_lazy('users-list')

    def format_datetime(self, value):
        # Cette méthode est un helper permettant de formater une date en chaine de caractères sous le même format que
        if value is not None:
            return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        return ""

    def test_list(self):
        user = User.objects.create(email='test@gmail.com', first_name='test', last_name='testing', age=23)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "profile": user.profile,
                "account_type": user.account_type,
                "is_active": user.is_active,
            }
        ]
        self.assertEqual(excepted, response.json())

    def test_create(self):
        self.assertFalse(User.objects.exists())
        response = self.client.post(self.url,
                                    data={"email": 'test@gmail.com', "first_name": 'test', "last_name": 'testing',
                                          "age": 23})
        # Vérifions que le status code est bien en erreur et nous empêche de créer un User
        self.assertEqual(response.status_code, 201)
        # Enfin, vérifions qu'aucune nouvelle catégorie n’a été créée malgré le status code 405

        self.assertTrue(User.objects.exists())
