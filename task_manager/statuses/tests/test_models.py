from django.test import TestCase
from task_manager.statuses.models import Status


# models test
class StatusModelTest(TestCase):
    def test_label_model(self):
        status = Status.objects.create(name='test')

        self.assertEqual(status.name, 'test')
        self.assertEqual(status.__str__(), 'test')
