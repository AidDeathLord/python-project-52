from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.labels.models import Label
from task_manager.mixins import UserLoginMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import LabelCreateForm
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from task_manager.tasks.models import Task
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
class LabelsView(UserLoginMixin, ListView):
    model = Label
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels'


class LabelsCreateView(UserLoginMixin, SuccessMessageMixin,
                       CreateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'context_form.html'
    success_url = reverse_lazy('labels')
    success_message = _('Метка успешно создана')
    extra_context = {'title': 'Создать метку',
                     'button_text': 'Создать'}


class LabelsUpdateView(UserLoginMixin, SuccessMessageMixin,
                       UpdateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'context_form.html'
    success_url = reverse_lazy('labels')
    success_message = _('Метка успешно изменена')
    extra_context = {'title': 'Изменение метки',
                     'button_text': 'Изменить'}


class LabelsDeleteView(UserLoginMixin,
                       SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    context_object_name = 'labels'
    success_url = reverse_lazy('labels')
    success_message = _('Метка успешно удалена')
    error_url = reverse_lazy('labels')
    error_message = _('Невозможно удалить метку, потому что она используется')

    def post(self, request, *args, **kwargs):
        label = Label.objects.get(pk=kwargs.get('pk'))
        try:
            Task.objects.get(label=label)
            messages.error(request, self.error_message)
            return redirect(self.error_url)
        except Task.DoesNotExist:
            return super().post(request, *args, **kwargs)
