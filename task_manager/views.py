from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _
from task_manager.users.forms import UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'context_form.html'
    success_message = _('Вы залогинены')
    form_class = UserLoginForm
    next_page = 'index'
    extra_context = {
        'title': _('Вход'),
        'button_text': _('Войти'),
    }


class UserLogoutView(SuccessMessageMixin, LogoutView):
    next_page = 'index'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('Вы разлогинены'))
        return super().dispatch(request, *args, **kwargs)
