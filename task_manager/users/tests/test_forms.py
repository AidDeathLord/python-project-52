from .tests_setup import UsersTests
from task_manager.users.forms import UserForm, UserUpdateForm

class UserFormsTest(UsersTests):
    def test_valid_form(self):
        form = UserForm(data=self.VALID_CREATE_USER)
        update_form = UserUpdateForm(data=self.VALID_CREATE_USER)

        self.assertTrue(form.is_valid())
        self.assertTrue(update_form.is_valid())

    def test_invalid_form(self):
        form = UserForm(data=self.MISSING_FIELDS_USER)
        update_form = UserUpdateForm(data=self.MISSING_FIELDS_USER)

        self.assertFalse(form.is_valid())
        self.assertFalse(update_form.is_valid())



