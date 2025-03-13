from django.urls import reverse_lazy
from task_manager.statuses.models import Status
from task_manager.statuses.tests.tests_setup import StatusesTests


class TestsStatusListView(StatusesTests):
    def test_status_view_logged_in_user(self):
        response = self.client.get(reverse_lazy('statuses'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                template_name='statuses/statuses_list.html')

    def test_status_view_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('statuses'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_statuses_content(self):
        response = self.client.get(reverse_lazy('statuses'))
        self.assertEqual(len(response.context['statuses']),
                         self.statuses_count)
        self.assertQuerySetEqual(
            response.context['statuses'],
            Status.objects.all(),
            ordered=False
        )

    def test_statuses_links(self):
        response = self.client.get(reverse_lazy('statuses'))

        self.assertContains(response, '/statuses/create/')
        self.assertContains(response, f'/statuses/{self.status1.id}/update/')
        self.assertContains(response, f'/statuses/{self.status1.id}/delete/')


class TestCreateView(StatusesTests):
    def test_sign_up_view(self):
        response = self.client.get(reverse_lazy('create_status'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                template_name='context_form.html')

    def test_statuses_view_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('create_status'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))


class TestUpdateView(StatusesTests):
    def test_update_view(self):

        response = self.client.get(
            reverse_lazy('update_status', kwargs={'pk': self.status1.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='context_form.html')

    def test_statuses_view_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('update_status', kwargs={'pk': self.status1.id}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))


class TestDeleteView(StatusesTests):
    def test_delete_view(self):
        response = self.client.get(
            reverse_lazy('delete_status', kwargs={'pk': self.status1.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='statuses/delete.html')

    def test_statuses_view_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('delete_status', kwargs={'pk': self.status1.id}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))
