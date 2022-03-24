from django.shortcuts import render

# Create your views here.


def get_menu(request):
    return render(request, 'reservation/menu.html')


def get_booking_form(request):
    return render(request, 'reservation/booking.html')
