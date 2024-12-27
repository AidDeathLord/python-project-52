from django.shortcuts import render, redirect
from django.views import View
from task_manager.tasks.models import Task
from .forms import CreateTaskForm
from django.utils.translation import gettext as _
from django.contrib import messages


# Create your views here.
class Tasks(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        context = {'tasks': tasks}
        return render(request, 'tasks/tasks_list.html', context=context)


class TaskCreate(View):

    def get(self, request, *args, **kwargs):
        form = CreateTaskForm
        context = {'form': form,
                   'title': _('Создать задачу'),
                   'button_text': _('Создать')}
        return render(request, 'context_form.html', context=context)

    def post(self, request, *args, **kwargs):
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.creator = request.user
            task.save()
            messages.success(request, _('Задача успешно создана'))
            return redirect('tasks')

        context = {'form': form,
                   'title': _('Создать задачу'),
                   'button_text': _('Создать')}
        return render(request, 'context_form.html', context=context)
