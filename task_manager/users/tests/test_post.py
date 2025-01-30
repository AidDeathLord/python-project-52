from django.test import TestCase
from task_manager.users.models import User
from django.urls import reverse_lazy
from django.test import Client
from django.utils.translation import gettext_lazy as _

from .users import (VALID_CREATE_USER,
                    MISSING_FIELDS_USER,
                    USER,
                    USER2,
                    USER2UPDATE)


class TestCreateUser(TestCase):

    def test_create_valid_user(self):
        response = self.client.post(reverse_lazy('create_user'),
                                    data=VALID_CREATE_USER)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertEqual(
            User.objects.last().username,
            VALID_CREATE_USER['username']
        )

    def test_create_fields_missing(self):
        response = self.client.post(reverse_lazy('create_user'),
                                    data=MISSING_FIELDS_USER)
        errors = response.context['form'].errors
        error_help = _('Обязательное поле.')

        self.assertIn('first_name', errors)
        self.assertEqual(
            [error_help],
            errors['first_name']
        )

        self.assertEqual(response.status_code, 200)


class TestUpdateUser(TestCase):
    client = Client()


    def test_update_self(self):
        user1 = User.objects.create_user(USER)
        user2 = User.objects.create_user(USER2['fields'])
        self.client.force_login(user1)

        response = self.client.post(
            reverse_lazy('update_user',
                         kwargs={'pk': user1.id}),
            data=USER2UPDATE
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))

        self.assertEqual(
            User.objects.get(pk=user1.id).first_name,
            USER2UPDATE['first_name']
        )

    # def test_update_other(self):
    #     self.client.force_login(self.user1)
    #
    #     response = self.client.post(
    #         reverse_lazy('update_user', kwargs={'pk': self.user2.id}),
    #         data=USER2UPDATE
    #     )
    #
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, reverse_lazy('users'))
    #
    #     self.assertNotEqual(
    #         User.objects.get(pk=101).first_name,
    #         USER2UPDATE['first_name']
    #     )


# class TestDeleteUser(TestCase):
#     def test_delete_self(self):
#         self.client.force_login(USER2)
#
#         response = self.client.post(
#             reverse_lazy('user_delete', kwargs={'pk': 100})
#         )
#
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse_lazy('users'))
#         with self.assertRaises(ObjectDoesNotExist):
#             User.objects.get(pk=100)
