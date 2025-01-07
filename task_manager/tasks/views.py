from django.shortcuts import render, redirect
from django.views import View
from task_manager.tasks.models import Task
from .forms import CreateTaskForm
from django.utils.translation import gettext as _
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from task_manager.mixins import CheckUserLoginMixin, CheckUserPermissionMixin


# Create your views here.
class Tasks(CheckUserLoginMixin, ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'


class TaskCreate(CheckUserLoginMixin, CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'context_form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Статус успешно создан')
    extra_context = {'title': 'Создать статус',
                     'button_text': 'Создать'}


class TaskUpdate(CheckUserLoginMixin, UpdateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'context_form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Статус успешно изменен')
    extra_context = {'title': 'Изменение статуса',
                     'button_text': 'Изменить'}


class TaskDelete(CheckUserLoginMixin, DeleteView):
    model = Task
    template_name = ''