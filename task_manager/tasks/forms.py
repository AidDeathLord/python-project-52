from django import forms
from .models import Task
from django.utils.translation import gettext as _


class CreateTaskForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Описание')}),
                                  label=_('Описание'))

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'executor', 'label']
