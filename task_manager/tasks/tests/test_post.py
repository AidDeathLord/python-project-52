from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from .tests_setup import TasksTests



class TestTask(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='Test User', password='123')
        self.client.login(username='Test User', password='123')

        self.test_status = Status.objects.create(name='Test Status')
        self.test_label = Label.objects.create(name='Test Label')

        self.count = Task.objects.count()
        self.task1 = {
            'title': 'Test Task',
            'description': 'Test Description',
            'creator': self.test_user.id,
            'status': self.test_status.id,
            'executor': self.test_user.id,
            'label': [self.test_label.id]
        }

    def test_create_valid_task(self):
        response = self.client.post(
            reverse_lazy('create_task'),
            data=self.task1
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))

        self.assertEqual(Task.objects.count(), self.count + 1)
        self.assertEqual(Task.objects.last().title, 'Test Task')
        self.assertEqual(Task.objects.last().creator, self.test_user)
        self.assertEqual(Task.objects.last().executor, self.test_user)

    # def test_create_fields_missing_task(self):
    #     response = self.client.post(reverse_lazy('create_task'),
    #                                 data={'title': '',
    #                                       'description': '',
    #                                       'executor': '',
    #                                       'status': ''})
    #     errors = response.context['form'].errors
    #     error_help = 'Обязательное поле.'
    #
    #     self.assertIn('title', errors)
    #     self.assertEqual([error_help], errors['title'])
    #
    #     self.assertIn('status', errors)
    #     self.assertEqual([error_help], errors['status'])
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(Task.objects.count(), self.count)
    #
    # def test_create_task_exists(self):
    #     response = self.client.post(reverse_lazy('create_task'),
    #                                 data={'title': 'Test Task',
    #                                       'description': 'Test Task',
    #                                       'executor': 1,
    #                                       'status': 1})
    #     errors = response.context['form'].errors
    #
    #     self.assertIn('title', errors)
    #     self.assertEqual(['Задача с таким Имя уже существует.'], errors['title'])
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(Task.objects.count(), self.count)


class TestUpdateTask(TasksTests):
    def test_update_task(self):
        response = self.client.post(
            reverse_lazy('update_task', kwargs={'pk': 2}),
            data={'title': 'Test Task22',
                  'description': 'Test Task22',
                  'executor': 2,
                  'status': 1})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))

        self.assertEqual(Task.objects.count(), self.count)
        self.assertEqual(
            Task.objects.get(id=self.task2.id).title, 'Test Task22')
        self.assertEqual(
            Task.objects.get(id=self.task2.id).executor.id, 2)

    def test_update_task_not_logged_in(self):
        self.client.logout()

        response = self.client.post(
            reverse_lazy('update_task', kwargs={'pk': 2}),
            data={'title': 'Test Task22',
                  'description': 'Test Task22',
                  'executor': 2,
                  'status': 1})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        self.assertEqual(Task.objects.count(), self.count)
        self.assertEqual(
            Task.objects.get(id=self.task2.id).title, 'Test Task2')


class TestDeleteTask(TasksTests):
    def test_delete_task(self):
        response = self.client.post(reverse_lazy('delete_task', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))
        self.assertEqual(Task.objects.count(), self.count - 1)
        with self.assertRaises(ObjectDoesNotExist):
            Task.objects.get(id=self.task1.id)

    def test_delete_task_not_logged_in(self):
        self.client.logout()

        response = self.client.post(
            reverse_lazy('delete_task', kwargs={'pk': 1})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertEqual(Task.objects.count(), self.count)

    def test_delete_task_unauthorised(self):
        response = self.client.post(reverse_lazy('delete_task', kwargs={'pk': 3}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))
        self.assertEqual(Task.objects.count(), self.count)
