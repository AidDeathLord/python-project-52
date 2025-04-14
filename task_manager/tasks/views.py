from task_manager.tasks.models import Task
from .forms import CreateTaskForm
from django.utils.translation import gettext as _
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from django.urls import reverse_lazy
from task_manager.mixins import UserLoginMixin, ProtectDeleteMixin, AuthorDeletionMixin
from django.contrib.messages.views import SuccessMessageMixin
from .filters import TaskFilter


# Create your views here.
class TasksView(UserLoginMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    extra_context = {'button_text': 'Показать'}


class TaskCreateView(UserLoginMixin, SuccessMessageMixin,
                     CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'context_form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Задача успешно создана')
    extra_context = {'title': 'Создать задачу',
                     'button_text': 'Создать'}

    def form_valid(self, form):
        self.creator = self.request.user
        form.instance.creator = self.creator
        return super().form_valid(form)


class TaskUpdateView(UserLoginMixin, SuccessMessageMixin,
                     UpdateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'context_form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Задача успешно изменена')
    extra_context = {'title': 'Изменение задачи',
                     'button_text': 'Изменить'}


class TaskDeleteView(UserLoginMixin, ProtectDeleteMixin,
                     SuccessMessageMixin, AuthorDeletionMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Задача успешно удалена')
    creator_message = _('Задачу может удалить только ее автор')
    creator_url = reverse_lazy('tasks')


class TaskShowView(UserLoginMixin, DetailView):
    model = Task
    template_name = 'tasks/task_show.html'
    context_object_name = 'task'
