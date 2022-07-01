from django.shortcuts import render


def menu(request):
    """ View to get menu """

    return render(request, 'menu/menu.html')
