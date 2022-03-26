from django.shortcuts import render

# Create your views here.


def get_index(request):
    return render(request, 'reservation/index.html')


def get_booking_form(request):
    return render(request, 'reservation/booking.html')
