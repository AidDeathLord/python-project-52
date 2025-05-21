from task_manager.tasks.forms import CreateTaskForm
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label

from django.test import TestCase
from dotenv import load_dotenv
import os

load_dotenv()


class TaskCreateFormTest(TestCase):
    USERNAME = os.getenv('TEST_USERNAME')
    PASWRD = os.getenv('TEST_PASSWORD')

    def setUp(self):
        self.test_user = User.objects.create_user(
            username=self.USERNAME,
            password=self.PASWRD
        )
        self.client.login(
            username=self.USERNAME,
            password=self.PASWRD
        )

        self.test_status = Status.objects.create(name='Test Status')
        self.test_label = Label.objects.create(name='Test Label')

    def test_task_form_valid(self):
        task = {
            'name': 'Test Task',
            'description': 'Test Description',
            'creator': self.test_user.id,
            'status': self.test_status.id,
            'executor': self.test_user.id,
            'labels': [self.test_label.id]
        }

        form = CreateTaskForm(data=task)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        task = {
            'name': '',
            'description': '',
            'creator': self.test_user.id,
            'status': '',
            'executor': self.test_user.id,
            'labels': self.test_label.id
        }

        form = CreateTaskForm(data=task)
        self.assertFalse(form.is_valid())
