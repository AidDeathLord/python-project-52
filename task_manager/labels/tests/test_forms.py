from django.test import TestCase
from task_manager.labels.forms import LabelCreateForm


class LabelCreateFormTest(TestCase):
    def test_label_form_valid(self):
        form = LabelCreateForm(data={'title': 'test'})

        self.assertTrue(form.is_valid())

    def test_label_form_invalid(self):
        form = LabelCreateForm(data={'title': ''})

        self.assertFalse(form.is_valid())
