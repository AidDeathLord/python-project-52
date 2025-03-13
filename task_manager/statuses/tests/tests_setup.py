from django.test import TestCase
from task_manager.users.models import User
from task_manager.statuses.models import Status


class StatusesTests(TestCase):
    USER = {"first_name": "Alan",
            "last_name": "Sapid",
            "username": "BestAlan",
            "password": "3Al"}

    def setUp(self):
        self.user = User.objects.create_user(self.USER)
        self.status1 = Status.objects.create(name='TestStatus1')
        self.status2 = Status.objects.create(name='TestStatus2')
        self.statuses_count = Status.objects.count()

        self.client.force_login(self.user)
