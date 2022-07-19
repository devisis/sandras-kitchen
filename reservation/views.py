from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path
from .forms import ReservationForm
from.models import Reservation


def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/index.html')
        # else:
        #     return render(request, 'reservation_create.html', {'form': form})
            # redirect('home/index.html')

    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'reservation_create.html', context)


def reservation_details(request):
    form = Reservation.objects.all()
    context = {
        'form': form
    }
    return render(request, 'reservation_details.html', context)


def reservation_edit(request, res_id):
    reservation = get_object_or_404(Reservation, id=res_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_details')

    form = ReservationForm(instance=reservation)
    context = {
        'form': form
    }
    return render(request, 'reservation_edit.html', context)


def reservation_delete(request, res_id):
    reservation = get_object_or_404(Reservation, id=res_id)
    reservation.delete()

    return redirect('reservation_details')
