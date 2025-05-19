from django import forms
from .models import Task
from django.utils.translation import gettext as _

from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


# class CreateTaskForm(forms.ModelForm):
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={'placeholder': _('Описание')}),
#         label=_('Описание')
#     )
#
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'status', 'executor', 'label']
#         widgets = {
#             'status': forms.Select(),
#             'executor': forms.Select(),
#             'label': forms.SelectMultiple(),
#         }


class CreateTaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'placeholder': _('Имя')
            }
        ),
        label=_('Имя')
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Описание')
            }
        ),
        label=_('Описание')
    )

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label=_('Статус'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label=_('Исполнитель'),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    label = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        required=False,
        label=_('Метки'),
        widget=forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'})
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'executor', 'label']
    #
    # def init(self, *args, **kwargs):
    #     super().init(*args, **kwargs)
    #     self.fields['executor'].label_from_instance = (lambda u: f"{u.first_name} {u.last_name}")  # DEBUG: посмотри, какие метки опций генерятся
    #     print("DEBUG executor choices:", self.fields['executor'].choices)
