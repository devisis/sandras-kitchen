from django.views.generic.list import ListView

from .models import Menu


class MenuView(ListView):
    """ View to get menu """

    model = Menu
    template_name = 'menu/menu_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
