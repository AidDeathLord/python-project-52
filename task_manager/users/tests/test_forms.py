from django.test import TestCase
from task_manager.users.forms import UserForm, UserUpdateForm
from .users import (VALID_CREATE_USER,
                    MISSING_FIELDS_USER)

UPDATE_VALID = {"username": "BestAlan",
                "first_name": "Alan",
                "last_name": "Sapid",
                "password1": "TBB",
                "password2": "TBB"}

UPDATE_INVALID = {"username": "BestAlan",
                  "first_name": "",
                  "last_name": "",
                  "password1": "TBB",
                  "password2": "TBB"}


class UserFormsTest(TestCase):
    def test_valid_form(self) -> None:
        form = UserForm(data=VALID_CREATE_USER)
        update_form = UserUpdateForm(data=VALID_CREATE_USER)

        self.assertTrue(form.is_valid())
        self.assertTrue(update_form.is_valid())

    def test_invalid_form(self) -> None:
        form = UserForm(data=MISSING_FIELDS_USER)
        update_form = UserUpdateForm(data=MISSING_FIELDS_USER)

        self.assertFalse(form.is_valid())
        self.assertFalse(update_form.is_valid())



