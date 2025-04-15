from django.urls import reverse_lazy

from .tests_setup import TasksTests


class TestsTasksListView(TasksTests):
    def test_tasks_view(self):
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

        self.assertContains(response, f'/tasks/{self.task1.id}/update/')
        self.assertContains(response, f'/tasks/{self.task1.id}/delete/')

    def test_tasks_not_logged_in_view(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('tasks'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))


class TestDetailedTask(TasksTests):
    def test_detailed_task_view(self):
        response = self.client.get(reverse_lazy('show_task', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='tasks/task_show.html'
        )

    def test_detailed_task_content(self):
        response = self.client.get(
            reverse_lazy('show_task', kwargs={'pk': 1})
        )

        labels = self.task1.label.all()

        self.assertContains(response, '/tasks/1/update/')
        self.assertContains(response, '/tasks/1/delete/')

        self.assertContains(response, self.task1.title)
        self.assertContains(response, self.task1.description)
        self.assertContains(response, self.task1.creator.first_name)
        self.assertContains(response, self.task1.executor.first_name)
        self.assertContains(response, self.task1.status)

        for label in labels:
            self.assertContains(response, label.title)

    def test_detailed_task_not_logged_in(self):
        self.client.logout()

        response = self.client.get(
            reverse_lazy('show_task', kwargs={'pk': 1})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))


class TestCreateTaskView(TasksTests):
    def test_create_task_view(self):
        response = self.client.get(reverse_lazy('create_task'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='context_form.html')

    def test_create_task_not_logged_in_view(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('create_task'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))


class TestUpdateTaskView(TasksTests):
    def test_update_task_view(self):
        response = self.client.get(reverse_lazy('update_task', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='context_form.html')

    def test_update_not_logged_in_view(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('update_task', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))


class TestDeleteTaskView(TasksTests):
    def test_delete_task_view(self):
        response = self.client.get(reverse_lazy('delete_task', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='tasks/delete.html')

    def test_delete_task_not_logged_in_view(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('delete_task', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))


class TestFilterTasks(TasksTests):
    def test_filter_tasks_status(self):
        response = self.client.get(reverse_lazy('tasks'),
                                   {'status': self.status1.pk})

        self.assertEqual(response.context['tasks'].count(), 2)
        self.assertContains(response, self.task1.title)
        self.assertContains(response, self.task2.title)
        self.assertNotContains(response, self.task3.title)

    def test_filter_tasks_executor(self):
        response = self.client.get(reverse_lazy('tasks'), {'executor': self.user2.pk})

        self.assertEqual(response.context['tasks'].count(), 2)
        self.assertContains(response, self.task1.title)
        self.assertContains(response, self.task2.title)
        self.assertNotContains(response, self.task3.title)
