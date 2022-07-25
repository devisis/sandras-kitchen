from django.shortcuts import render
from django.views.generic.list import ListView

from menu.models import Menu


class IndexListView(ListView):

    model = Menu
    template_name = 'home/index.html'

    # Get object data and return it
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
