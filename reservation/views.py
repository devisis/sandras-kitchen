from django.shortcuts import render, HttpResponse

# Create your views here.


def say_hello(request):
    return HttpResponse("hello")

# def get_menu(request):
#     return render(request, 'menu/menu.html')


# def get_booking_form(request):
#     return render(request, 'booking/booking.html')
