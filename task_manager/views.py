from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.utils.translation import gettext as _


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')
