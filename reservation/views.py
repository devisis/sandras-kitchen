from django.shortcuts import render

# Create your views here.


def get_index(request):
    return render(request, 'index.html')


def get_booking_form(request):
    return render(request, 'booking.html')
