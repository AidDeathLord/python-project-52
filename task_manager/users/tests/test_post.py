from task_manager.users.models import User
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from .tests_setup import UsersTests


class TestCreateUser(UsersTests):

    def test_create_valid_user(self):
        response = self.client.post(reverse_lazy('create_user'),
                                    data=self.VALID_CREATE_USER)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertEqual(User.objects.last().username,
                         self.VALID_CREATE_USER['username'])

    def test_create_fields_missing(self):
        response = self.client.post(reverse_lazy('create_user'),
                                    data=self.MISSING_FIELDS_USER)
        errors = response.context['form'].errors
        error_help = _('Обязательное поле.')

        self.assertIn('first_name', errors)
        self.assertEqual([error_help],
                         errors['first_name'])
        self.assertEqual(response.status_code, 200)


class TestUpdateUser(UsersTests):

    def test_update_self(self):
        self.client.force_login(self.user1)

        response = self.client.post(
            reverse_lazy('update_user',
                         kwargs={'pk': self.user1.id}),
            data=self.USER1UPDATE)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))

        self.assertEqual(User.objects.get(pk=self.user1.id).first_name,
                         self.USER1UPDATE['first_name'])

    def test_update_other(self):
        self.client.force_login(self.user1)

        response = self.client.post(
            reverse_lazy('update_user',
                         kwargs={'pk': self.user2.id}),
            data=self.USER2UPDATE
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))
        self.assertNotEqual(
            User.objects.get(pk=self.user2.id).first_name,
            self.USER2UPDATE['first_name']
        )


class TestDeleteUser(UsersTests):

    def test_delete_self(self):
        self.client.force_login(self.user1)

        response = self.client.post(
            reverse_lazy('delete_user',
                         kwargs={'pk': self.user1.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(pk=self.user1.id)

    def test_delete_other(self):
        self.client.force_login(self.user1)

        response = self.client.post(
            reverse_lazy('delete_user', kwargs={'pk': self.user2.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))
        self.assertEqual(User.objects.count(), self.users_count)
