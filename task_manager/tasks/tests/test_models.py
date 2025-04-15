from task_manager.tasks.models import Task
from .tests_setup import TasksTests


class TaskModelTest(TasksTests):
    def test_task_creation(self):
        task = Task.objects.create(
            title='Test Task4',
            description='Test description',
            creator=self.user1,
            status=self.status1,
            executor=self.user2,
        )
        task.label.set(self.label1)

        self.assertTrue(isinstance(task, Task))
        self.assertEqual(task.__str__(), 'Test Task4')
        self.assertEqual(task.title, 'Test Task4')
        self.assertEqual(task.description, 'Test description')
        self.assertEqual(task.creator, self.user1)
        self.assertEqual(task.status, self.status1)
        self.assertEqual(task.executor, self.user2)
        self.assertEqual(task.label.get(pk=1), self.label)
