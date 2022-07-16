from django.shortcuts import render, redirect
from django.urls import path
from .forms import ReservationForm
from.models import Reservation
from django.views.generic import ListView


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/index.html')
        else:
            return render(request, 'reservation.html', {'form': form})
            # redirect('home/index.html')

    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'reservation.html', context)


class EditReservations(ListView):
    model = Reservation
