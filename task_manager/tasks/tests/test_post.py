from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TestTask(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='Test User',
            password='123' #NOSONAR
        )
        self.test_user2 = User.objects.create_user(
            username='Test User2',
            password='123' #NOSONAR
        )
        self.client.login(
            username='Test User',
            password='123' #NOSONAR
        )

        self.test_status = Status.objects.create(name='Test Status')
        self.test_status2 = Status.objects.create(name='Test Status2')
        self.test_label = Label.objects.create(name='Test Label')

        self.test_task = Task.objects.create(
            name='Test Task 22',
            description='Test Task 22',
            creator=self.test_user,
            status=self.test_status,
            executor=self.test_user,
        )
        self.test_task2 = Task.objects.create(
            name='Test Task 123',
            description='Test Task 123',
            creator=self.test_user,
            status=self.test_status,
            executor=self.test_user2,
        )
        self.test_task3 = Task.objects.create(
            name='Test Task 2222',
            description='Test Task 2222',
            creator=self.test_user2,
            status=self.test_status,
            executor=self.test_user2,
        )

        self.count = Task.objects.count()

        self.task1 = {
            'name': 'Test Task',
            'description': 'Test Description',
            'creator': self.test_user.id,
            'status': self.test_status.id,
            'executor': self.test_user.id,
            'labels': [self.test_label.id]
        }

        self.task2 = {
            'name': '',
            'description': '',
            'creator': self.test_user.id,
            'status': '',
            'executor': '',
            'labels': [self.test_label.id]
        }

        self.task3 = {
            'name': 'Test Task 22',
            'description': 'Test Task 22',
            'creator': self.test_user.id,
            'status': self.test_status.id,
            'executor': self.test_user.id,
        }

    def test_create_valid_task(self):
        response = self.client.post(
            reverse_lazy('create_task'),
            data=self.task1
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))

        self.assertEqual(Task.objects.count(), self.count + 1)
        self.assertEqual(Task.objects.last().name, 'Test Task')
        self.assertEqual(Task.objects.last().creator, self.test_user)
        self.assertEqual(Task.objects.last().executor, self.test_user)

    def test_create_fields_missing_task(self):
        response = self.client.post(
            reverse_lazy('create_task'),
            data=self.task2
        )
        errors = response.context['form'].errors
        error_help = 'Обязательное поле.'

        self.assertIn('name', errors)
        self.assertEqual([error_help], errors['name'])

        self.assertIn('status', errors)
        self.assertEqual([error_help], errors['status'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), self.count)

    def test_create_task_exists(self):
        response = self.client.post(
            reverse_lazy('create_task'),
            data=self.task3
        )
        errors = response.context['form'].errors

        self.assertIn('name', errors)
        self.assertEqual(['Задача с таким Имя уже существует.'], errors['name'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), self.count)

    def test_update_task(self):
        response = self.client.post(
            reverse_lazy('update_task', kwargs={'pk': self.test_task2.id}),
            data={
                'name': 'Test Task 1234',
                'description': 'Test Task 1234',
                'creator': self.test_user.id,
                'status': self.test_status2.id,
                'executor': self.test_user.id,
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))

        self.assertEqual(Task.objects.count(), self.count)
        self.assertEqual(
            Task.objects.get(id=self.test_task2.id).name,
            'Test Task 1234'
        )
        self.assertEqual(
            Task.objects.get(id=self.test_task2.id).executor.id,
            self.test_user.id
        )

    def test_update_task_not_logged_in(self):
        self.client.logout()

        response = self.client.post(
            reverse_lazy('update_task', kwargs={'pk': self.test_task2.id}),
            data={
                'name': 'Test Task 2221',
                'description': 'Test Task 2221',
                'creator': self.test_user.id,
                'status': self.test_status2.id,
                'executor': self.test_user2.id,
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        self.assertEqual(Task.objects.count(), self.count)
        self.assertEqual(
            Task.objects.get(id=self.test_task2.id).name, 'Test Task 123')

    def test_delete_task(self):
        response = self.client.post(
            reverse_lazy('delete_task', kwargs={'pk': self.test_task2.id}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))
        self.assertEqual(Task.objects.count(), self.count - 1)
        with self.assertRaises(ObjectDoesNotExist):
            Task.objects.get(id=self.test_task2.id)

    def test_delete_task_not_logged_in(self):
        self.client.logout()

        response = self.client.post(
            reverse_lazy('delete_task', kwargs={'pk': self.test_task2.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertEqual(Task.objects.count(), self.count)

    def test_delete_task_unauthorised(self):
        response = self.client.post(
            reverse_lazy('delete_task', kwargs={'pk': self.test_task3.id}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))
        self.assertEqual(Task.objects.count(), self.count)
