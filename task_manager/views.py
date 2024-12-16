from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _
from task_manager.users.forms import UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = _('Вы залогинены')
    form_class = UserLoginForm
    next_page = 'index'


class UserLogoutView(SuccessMessageMixin, LogoutView):
    next_page = 'index'
    success_message = _('You have been logged out.')
