from django.urls import reverse_lazy
from django.test import TestCase

from task_manager.users.models import User
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label

from dotenv import load_dotenv
import os


load_dotenv()


class TestsTasksView(TestCase):
    USERNAME = os.getenv('TEST_USERNAME')
    USERNAME2 = os.getenv('TEST_USERNAME2')
    PASWRD = os.getenv('TEST_PASSWORD')

    def setUp(self):
        self.test_user = User.objects.create_user(
            username=self.USERNAME,
            password=self.PASWRD
        )
        self.test_user2 = User.objects.create_user(
            username=self.USERNAME2,
            password=self.PASWRD
        )
        self.client.login(
            username=self.USERNAME,
            password=self.PASWRD
        )

        self.test_status = Status.objects.create(name='Test Status')
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

        self.count = Task.objects.count()
        self.tasks = Task.objects.all()

    def test_tasks_list_view(self):
        response = self.client.get(reverse_lazy('tasks'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                template_name='tasks/tasks_list.html')

    def test_tasks_content(self):
        response = self.client.get(reverse_lazy('tasks'))

        self.assertEqual(len(response.context['tasks']), self.count)
        self.assertQuerySetEqual(response.context['tasks'],
                                 self.tasks,
                                 ordered=False)

    def test_tasks_links(self):
        response = self.client.get(reverse_lazy('tasks'))

        self.assertContains(response, '/tasks/create/')

        self.assertContains(response, f'/tasks/{self.test_task.id}/update/')
        self.assertContains(response, f'/tasks/{self.test_task.id}/delete/')

    def test_tasks_not_logged_in_view(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('tasks'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_detailed_task_view(self):
        response = self.client.get(
            reverse_lazy('show_task', kwargs={'pk': self.test_task.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='tasks/task_show.html'
        )

    def test_detailed_task_content(self):
        self.test_task.labels.add(self.test_label)

        response = self.client.get(
            reverse_lazy('show_task', kwargs={'pk': self.test_task.id})
        )

        self.assertContains(response, f'/tasks/{self.test_task.id}/update/')
        self.assertContains(response, f'/tasks/{self.test_task.id}/delete/')

        self.assertContains(response, self.test_task.name)
        self.assertContains(response, self.test_task.description)
        self.assertContains(response, self.test_task.creator.first_name)
        self.assertContains(response, self.test_task.executor.first_name)
        self.assertContains(response, self.test_task.status.name)

        for label in self.test_task.labels.all():
            self.assertContains(response, label.name)

    def test_detailed_task_not_logged_in(self):
        self.client.logout()

        response = self.client.get(
            reverse_lazy('show_task', kwargs={'pk': self.test_task.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_create_task_view(self):
        response = self.client.get(reverse_lazy('create_task'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='context_form.html')

    def test_create_task_not_logged_in_view(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('create_task'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_task_view(self):
        response = self.client.get(
            reverse_lazy('update_task', kwargs={'pk': self.test_task.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='context_form.html')

    def test_update_not_logged_in_view(self):
        self.client.logout()

        response = self.client.get(
            reverse_lazy('update_task', kwargs={'pk': self.test_task.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_delete_task_view(self):
        response = self.client.get(
            reverse_lazy('delete_task', kwargs={'pk': self.test_task.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='tasks/delete.html')

    def test_delete_task_not_logged_in_view(self):
        self.client.logout()

        response = self.client.get(
            reverse_lazy('delete_task', kwargs={'pk': self.test_task.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_filter_tasks_status(self):
        response = self.client.get(reverse_lazy('tasks'),
                                   {'status': self.test_status.id})

        self.assertEqual(response.context['tasks'].count(), 2)
        self.assertContains(response, self.test_task.name)
        self.assertContains(response, self.test_task2.name)

    def test_filter_tasks_executor(self):
        response = self.client.get(
            reverse_lazy('tasks'), {'executor': self.test_user.pk}
        )

        self.assertEqual(response.context['tasks'].count(), 1)
        self.assertContains(response, self.test_task.name)
        self.assertNotContains(response, self.test_task2.name)
