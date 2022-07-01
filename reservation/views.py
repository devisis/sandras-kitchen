from django.shortcuts import render
from django.urls import path
# from .models import Customer,Table,Booking 


def reservation(request):
    return render(request, 'reservation.html')
