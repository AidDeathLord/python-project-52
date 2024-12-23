from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import User
from .forms import CreateUserForm
from django.utils.translation import gettext as _


class Users(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/users_list.html', context={'users': users})


class CreateUserView(View):

    def get(self, request, *args, **kwargs):
        form = CreateUserForm()
        context = {'form': form,
                   'title': 'Регистрация',
                   'button_text': 'Зарегистрировать'}
        return render(request, 'users/create_update.html', context=context)

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        context = {'form': form,
                   'title': 'Регистрация',
                   'button_text': 'Зарегистрировать'}
        return render(request, 'users/create_update.html', context=context)


class UpdateUserView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(User, id=user_id)
        form = CreateUserForm(instance=user)
        context = {'form': form,
                   'user_id': user_id,
                   'title': 'Изменение пользователя',
                   'button_text': 'Изменить'}
        return render(request, 'users/create_update.html', context=context)

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(User, id=user_id)
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')

        context = {'form': form,
                   'user_id': user_id,
                   'title': 'Изменение пользователя',
                   'button_text': 'Изменить'}
        return render(request, 'users/create_update.html', context=context)


class DeleteUserView(View):

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
