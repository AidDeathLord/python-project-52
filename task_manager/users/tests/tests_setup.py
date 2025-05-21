from django.test import TestCase
from task_manager.users.models import User


class UsersTests(TestCase):

    VALID_CREATE_USER = {"username": "BestAlan",
                         "first_name": "Alan",
                         "last_name": "Sapid",
                         "password1": "3Al",  # NOSONAR
                         "password2": "3Al"}  # NOSONAR

    MISSING_FIELDS_USER = {"username": "BestAlan",
                           "first_name": "",
                           "last_name": "",
                           "password1": "3Al",  # NOSONAR
                           "password2": "3Al"}  # NOSONAR

    USER1 = {"first_name": "Alan",
             "last_name": "Sapid",
             "username": "BestAlan",
             "password": "3Al"}  # NOSONAR

    USER1UPDATE = {"username": "AidD",
                   "first_name": "Alan",
                   "last_name": "Sapid",
                   "password1": "3Al",  # NOSONAR
                   "password2": "3Al"}  # NOSONAR

    USER2 = {"first_name": "Qwerty",
             "last_name": "Qwer",
             "username": "123123",
             "password": "12345"}  # NOSONAR

    USER2UPDATE = {"first_name": "Qwerty",
                   "last_name": "Qwer",
                   "username": "3323",
                   "password1": "12345",  # NOSONAR
                   "password2": "12345"}  # NOSONAR

    def setUp(self):
        self.user1 = User.objects.create_user(self.USER1)
        self.user2 = User.objects.create_user(self.USER2)
        self.users_count = User.objects.count()
