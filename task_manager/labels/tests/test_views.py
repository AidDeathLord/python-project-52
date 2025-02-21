from django.urls import reverse_lazy
from task_manager.labels.models import Label
from task_manager.labels.tests.tests_setup import LabelsTests


class TestsListView(LabelsTests):
    def test_labels_view_logged_in_user(self):
        response = self.client.get(reverse_lazy('labels'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                template_name='labels/labels_list.html')

    def test_labels_view_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('labels'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_labels_content(self):
        response = self.client.get(reverse_lazy('labels'))
        self.assertEqual(len(response.context['labels']),
                         self.labels_count)
        self.assertQuerySetEqual(
            response.context['labels'],
            Label.objects.all(),
            ordered=False
        )

    def test_labels_links(self):
        response = self.client.get(reverse_lazy('labels'))

        self.assertContains(response, '/labels/create/')
        self.assertContains(response, f'/labels/{self.label1.id}/update/')
        self.assertContains(response, f'/labels/{self.label1.id}/delete/')


class TestCreateView(LabelsTests):
    def test_sign_up_view(self):
        response = self.client.get(reverse_lazy('create_label'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                template_name='context_form.html')

    def test_labels_view_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('create_label'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))


class TestUpdateView(LabelsTests):
    def test_update_view(self):

        response = self.client.get(
            reverse_lazy('update_label', kwargs={'pk': self.label1.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='context_form.html')

    def test_labels_view_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('update_label', kwargs={'pk': self.label1.id}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))


class TestDeleteView(LabelsTests):
    def test_delete_view(self):
        response = self.client.get(
            reverse_lazy('delete_label', kwargs={'pk': self.label1.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='labels/delete.html')

    def test_labels_view_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('delete_label', kwargs={'pk': self.label1.id}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))
