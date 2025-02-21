from task_manager.labels.models import Label
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from .tests_setup import LabelsTests


class TestCreateLabel(LabelsTests):

    def test_create_label(self):
        response = self.client.post(reverse_lazy('create_label'),
                                    data={'name': 'TestLabel3'})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels'))
        self.assertEqual(Label.objects.last().name, 'TestLabel3')

    def test_create_label_fields_missing(self):
        response = self.client.post(reverse_lazy('create_label'),
                                    data={'name': ''})

        errors = response.context['form'].errors
        self.assertEqual(response.status_code, 200)
        self.assertIn('name', errors)


class TestUpdateLabel(LabelsTests):

    def test_update_label(self):
        response = self.client.post(
            reverse_lazy('update_label',
                         kwargs={'pk': self.label1.id}),
            data={'name': 'TestLabel11'})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels'))

        self.assertEqual(Label.objects.get(pk=self.label1.id).name,
                         'TestLabel11')


class TestDeleteLabel(LabelsTests):

    def test_delete_label(self):
        response = self.client.post(
            reverse_lazy('delete_label',
                         kwargs={'pk': self.label1.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels'))
        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(pk=self.label1.id)
