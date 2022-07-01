from django.shortcuts import render


from django.shortcuts import render

def index(request):
    """ A view to return my index page """

    return render(request, "home/index.html")
