from task_manager.statuses.models import Status
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from .tests_setup import StatusesTests


class TestCreateStatus(StatusesTests):

    def test_create_valid_status(self):
        response = self.client.post(reverse_lazy('create_status'),
                                    data={'name': 'TestStatus10'})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses'))
        self.assertEqual(Status.objects.last().name, "TestStatus10")

    def test_create_fields_missing(self):
        response = self.client.post(reverse_lazy('create_status'),
                                    data={'name': ''})
        errors = response.context['form'].errors
        error_help = _('Обязательное поле.')

        self.assertIn('name', errors)
        self.assertEqual([error_help],
                         errors['name'])
        self.assertEqual(response.status_code, 200)


class TestUpdateStatus(StatusesTests):

    def test_update_status(self):
        response = self.client.post(
            reverse_lazy('update_status',
                         kwargs={'pk': self.status1.id}),
            data={'name': 'TestStatus11'})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses'))

        self.assertEqual(Status.objects.get(pk=self.status1.id).name,
                         'TestStatus11')


class TestDeleteStatus(StatusesTests):

    def test_delete_status(self):
        response = self.client.post(
            reverse_lazy('delete_status',
                         kwargs={'pk': self.status1.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses'))
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(pk=self.status1.id)
