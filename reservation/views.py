from django.shortcuts import render
from django.urls import path
import requests
# from .models import Customer,Table,Booking 


def reservation(request):
    # context = {}
    return render(request, 'reservation.html')


def request_reservation(request):
    if request.method == "POST":
        pickPartySize
        pickDate
        pickTime
