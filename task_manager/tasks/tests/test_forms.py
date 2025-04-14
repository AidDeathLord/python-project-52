from .tests_setup import TasksTests
from task_manager.tasks.forms import CreateTaskForm


class TaskCreateFormTest(TasksTests):
    def test_task_form_valid(self):
        form = CreateTaskForm(data={'title': 'Test Task5',
                                    'description': 'Test Task',
                                    'executor':1,
                                    'status': 1})

        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        form = CreateTaskForm(data={'title': 'Test Task',
                                    'description': '',
                                    'executor': '',
                                    'status': 1})

        self.assertFalse(form.is_valid())
