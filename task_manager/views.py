from django.shortcuts import render, redirect
from django.views import View
from django.utils.translation import gettext as _
from task_manager.users.forms import LoginForm
from django.contrib.auth.views import LoginView, LogoutView


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    next_page = 'index'


    # def get(self, request, *args, **kwargs):
    #     form = LoginForm()
    #     return render(request, 'login.html', context={'form': form})
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('index')
    #
    #     return redirect('login')
