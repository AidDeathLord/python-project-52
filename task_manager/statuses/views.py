from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Status
from .forms import CreateStatusForm
from django.utils.translation import gettext as _
from django.contrib import messages
from task_manager.mixins import CheckUserLoginMixin


# Create your views here.
class Statuses(CheckUserLoginMixin, View):

    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(request, 'statuses/statuses_list.html',
                      context={'statuses': statuses})


class CreateStatus(CheckUserLoginMixin, View):

    def get(self, request, *args, **kwargs):
        form = CreateStatusForm
        context = {'form': form,
                   'title': _('Создать статус'),
                   'button_text': _('Создать')}
        return render(request, 'context_form.html', context=context)

    def post(self, request, *args, **kwargs):
        form = CreateStatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Статус успешно создан'))
            return redirect('statuses')

        context = {'form': form,
                   'title': _('Создать статус'),
                   'button_text': _('Создать')}
        return render(request, 'context_form.html', context=context)


class UpdateStatus(CheckUserLoginMixin, View):

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = get_object_or_404(Status, id=status_id)
        form = CreateStatusForm(instance=status)
        context = {'form': form,
                   'status_id': status_id,
                   'title': 'Изменение статуса',
                   'button_text': 'Изменить'}
        return render(request, 'context_form.html', context=context)

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = get_object_or_404(Status, id=status_id)
        form = CreateStatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, _('Статус успешно изменен'))
            return redirect('statuses')

        context = {'form': form,
                   'status_id': status_id,
                   'title': 'Изменение статуса',
                   'button_text': 'Изменить'}
        return render(request, 'context_form.html', context=context)


class DeleteStatus(CheckUserLoginMixin, View):

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = get_object_or_404(Status, id=status_id)
        context = {'status': f'{status.name}',
                   'status_id': status_id}
        return render(request, 'statuses/delete.html', context=context)

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        if status:
            status.delete()
            messages.success(request, _('Статус успешно удален'))
            return redirect('statuses')
        messages.error(request, _('Статуса не существует'))
        return redirect('statuses')
