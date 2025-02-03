from django.urls import reverse_lazy
from task_manager.users.models import User
from .tests_setup import UsersTests


class TestsListView(UsersTests):
    def test_users_view(self):
        response = self.client.get(reverse_lazy('users'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                template_name='users/users_list.html')

    def test_users_content(self):
        response = self.client.get(reverse_lazy('users'))
        self.assertEqual(len(response.context['users']),
                         User.objects.count())
        self.assertQuerySetEqual(
            response.context['users'],
            User.objects.all(),
            ordered=False
        )

    def test_links(self):
        response = self.client.get(reverse_lazy('users'))

        self.assertContains(response, '/users/create/')
        self.assertContains(response, f'/users/{self.user1.id}/update/')
        self.assertContains(response, f'/users/{self.user1.id}/delete/')


class TestCreateView(UsersTests):
    def test_sign_up_view(self):
        response = self.client.get(reverse_lazy('create_user'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                template_name='context_form.html')


class TestUpdateView(UsersTests):
    def test_update_self_view(self):
        self.client.force_login(self.user1)

        response = self.client.get(
            reverse_lazy('update_user', kwargs={'pk': self.user1.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='context_form.html')

    def test_update_not_logged_in_view(self):
        response = self.client.get(
            reverse_lazy('update_user', kwargs={'pk': self.user1.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_other_view(self) -> None:
        self.client.force_login(self.user1)

        response = self.client.get(
            reverse_lazy('update_user', kwargs={'pk': self.user2.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))
