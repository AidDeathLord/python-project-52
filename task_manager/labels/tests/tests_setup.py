from django.test import TestCase
from task_manager.users.models import User
from task_manager.labels.models import Label


class LabelsTests(TestCase):
    USER = {"first_name": "Alan",
            "last_name": "Sapid",
            "username": "BestAlan",
            "password": "3Al"}

    def setUp(self):
        self.user = User.objects.create_user(self.USER)
        self.label1 = Label.objects.create(name='TestLabel1')
        self.label2 = Label.objects.create(name='TestLabel2')
        self.labels_count = Label.objects.count()

        self.client.force_login(self.user)
