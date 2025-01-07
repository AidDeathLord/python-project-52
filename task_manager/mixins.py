from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.translation import gettext as _
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


class CheckUserLoginMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('Вы не авторизованы! Пожалуйста, выполните вход.'))
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


class CheckUserPermissionMixin(UserPassesTestMixin):
    permission_message = _('У вас нет прав для изменения другого пользователя.')
    permission_url = reverse_lazy('users')

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(self.request, self.permission_message)
        return redirect(self.permission_url)