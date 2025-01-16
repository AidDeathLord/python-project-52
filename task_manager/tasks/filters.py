from django_filters import FilterSet, BooleanFilter
from django import forms
from .models import Task
from django.utils.translation import gettext as _


class TaskFilter(FilterSet):
    logged_in_user = BooleanFilter(label=_('Только свои задачи'),
                                   widget=forms.CheckboxInput,
                                   method='get_user_tasks')

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label', 'logged_in_user']

    def get_user_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(creator=user)
        return queryset


