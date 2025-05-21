from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import User
from .forms import UserForm, UserUpdateForm
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from task_manager.mixins import (UserLoginMixin,
                                 UserDeletePermissionMixin,
                                 ProtectDeleteMixin)


class UsersListView(ListView):
    template_name = 'users/users_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_staff=0)


class UsersCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    model = User
    template_name = 'context_form.html'
    success_url = reverse_lazy('login')
    success_message = _('Пользователь успешно зарегистрирован')
    extra_context = {'title': 'Регистрация',
                     'button_text': 'Зарегистрировать'}


class UsersUpdateView(UserLoginMixin, UserDeletePermissionMixin,
                      SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'context_form.html'
    success_url = reverse_lazy('users')
    form_class = UserUpdateForm
    success_message = _('Пользователь успешно изменен')
    extra_context = {'title': 'Изменение пользователя',
                     'button_text': 'Изменить'}


class UsersDeleteView(UserLoginMixin, UserDeletePermissionMixin,
                      ProtectDeleteMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _('Пользователь успешно удален')
    error_message = _(
        'Невозможно удалить пользователя, потому что он используется'
    )
    error_url = reverse_lazy('users')
