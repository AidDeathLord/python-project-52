from .tests_setup import UsersTests
from task_manager.users.models import User


# models test
class UserModelTest(UsersTests):
    def test_user_model(self):
        user = User.objects.create(
            username=self.USER1['username'],
            first_name=self.USER1['first_name'],
            last_name=self.USER1['last_name'],
            password=self.USER1['password']
        )

        self.assertEqual(user.first_name, 'Alan')
        self.assertEqual(user.last_name, 'Sapid')
        self.assertEqual(user.username, 'BestAlan')
        self.assertEqual(user.password, '3Al')
        self.assertEqual(user.__str__(), 'Alan Sapid')
