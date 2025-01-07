from .models import Status
from .forms import CreateStatusForm
from django.utils.translation import gettext as _
from task_manager.mixins import CheckUserLoginMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class Statuses(CheckUserLoginMixin, ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'


class StatusCreate(CheckUserLoginMixin, SuccessMessageMixin,
                   CreateView):
    model = Status
    template_name = 'context_form.html'
    form_class = CreateStatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Статус успешно создан')
    extra_context = {'title': _('Создать статус'),
                     'button_text': _('Создать')}


class StatusUpdate(CheckUserLoginMixin, SuccessMessageMixin,
                   UpdateView):
    model = Status
    template_name = 'context_form.html'
    form_class = CreateStatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Статус успешно изменен')
    extra_context = {'title': _('Изменение статуса'),
                     'button_text': _('Изменить')}


class StatusDelete(CheckUserLoginMixin, SuccessMessageMixin,
                   DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Статус успешно удален')
