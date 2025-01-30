from django.test import TestCase
from task_manager.users.models import User
from .users import USER


# models test
class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(**USER['fields'])

    def test_user_model(self):
        user = User.objects.get(id=1)

        self.assertEqual(user.first_name, 'Alan')
        self.assertEqual(user.last_name, 'Sapid')
        self.assertEqual(user.username, 'BestAlan')
        self.assertEqual(user.password, '3Al')
        self.assertEqual(user.__str__(), 'BestAlan')
