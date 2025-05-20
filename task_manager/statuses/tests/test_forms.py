from django.test import TestCase
from task_manager.statuses.forms import CreateStatusForm


class StatusCreateFormTest(TestCase):
    def test_label_form_valid(self):
        form = CreateStatusForm(data={'title': 'test'})

        self.assertTrue(form.is_valid())

    def test_label_form_invalid(self):
        form = CreateStatusForm(data={'title': ''})

        self.assertFalse(form.is_valid())
