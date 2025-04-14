from django.test import TestCase, Client

from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TasksTests(TestCase):
    USER1 = {"first_name": "Alan",
             "last_name": "Sapid",
             "username": "BestAlan",
             "password": "3Al"}

    USER2 = {"first_name": "Qwerty",
             "last_name": "Qwer",
             "username": "123123",
             "password": "12345"}

    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.create_user(self.USER1)
        self.user2 = User.objects.create_user(self.USER2)

        self.status1 = Status.objects.create(name='TestStatus1')
        self.status2 = Status.objects.create(name='TestStatus2')

        self.label = Label.objects.create(name='TestLabel')
        self.label1 = Label.objects.filter(pk=1)

        self.task1 = Task.objects.create(title='Test Task',
                                         description='Test Task',
                                         creator=self.user1,
                                         executor=self.user2,
                                         status=self.status1)
        self.task2 = Task.objects.create(title='Test Task2',
                                         description='Test Task2',
                                         creator=self.user2,
                                         executor=self.user2,
                                         status=self.status1)
        self.task3 = Task.objects.create(title='Test Task3',
                                         description='Test Task3',
                                         creator=self.user2,
                                         executor=self.user1,
                                         status=self.status2)

        self.tasks = Task.objects.all()
        self.count = Task.objects.count()

        self.client.force_login(self.user1)
