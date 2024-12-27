from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import User
from .forms import UserForm, UserUpdateForm
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from task_manager.mixins import CheckUserLoginMixin


class UsersListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class UsersCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    model = User
    template_name = 'context_form.html'
    success_url = reverse_lazy('login')
    success_message = _('Пользователь успешно зарегистрирован')
    extra_context = {'title': 'Регистрация',
                     'button_text': 'Зарегистрировать'}


class UsersUpdateView(SuccessMessageMixin, UpdateView,
                      CheckUserLoginMixin):
    template_name = 'context_form.html'
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('users')
    success_message = _('Пользователь успешно изменен')
    extra_context = {'title': 'Изменение пользователя',
                     'button_text': 'Изменить'}


class UserDelete(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(User, id=user_id)
        context = {'user': f'{user.first_name} {user.last_name}',
                   'user_id': user_id}
        return render(request, 'users/delete.html', context=context)

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        if user:
            user.delete()

        return redirect('users')
