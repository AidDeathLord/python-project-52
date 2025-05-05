from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from django.test import TestCase


class TaskModelTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='Test User', password='123')
        self.client.login(username='Test User', password='123')

        self.test_status = Status.objects.create(name='Test Status')

        self.test_task = Task.objects.create(
            title='Test Task',
            description='Test Task',
            creator=self.test_user,
            status=self.test_status,
            executor=self.test_user,
        )

    def test_task_creation(self):
        self.test_task.label.create(name='Test Label')

        self.assertTrue(isinstance(self.test_task, Task))
        self.assertEqual(self.test_task.__str__(), 'Test Task')
        self.assertEqual(self.test_task.title, 'Test Task')
        self.assertEqual(self.test_task.description, 'Test Task')
        self.assertEqual(self.test_task.creator, self.test_user)
        self.assertEqual(self.test_task.status, self.test_status)
        self.assertEqual(self.test_task.executor, self.test_user)
        self.assertEqual(str(self.test_task.label.get(pk=1)), 'Test Label')
