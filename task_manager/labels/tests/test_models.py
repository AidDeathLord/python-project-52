from django.test import TestCase
from task_manager.labels.models import Label


# models test
class LabelModelTest(TestCase):
    def test_label_model(self):
        label = Label.objects.create(name='test')

        self.assertEqual(label.name, 'test')
        self.assertEqual(label.__str__(), 'test')
