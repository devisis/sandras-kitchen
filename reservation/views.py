from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import path
from .forms import ReservationForm
from.models import Reservation


@login_required
def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reservation_details')

    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'reservation_create.html', context)


@login_required
def reservation_details(request):
    # form = Reservation.objects.filter(user=request.user)
    form = Reservation.objects.all()
    context = {
        'form': form
    }
    return render(request, 'reservation_details.html', context)


@login_required
def reservation_edit(request, res_id):
    reservation = get_object_or_404(Reservation, id=res_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            resveration.objects.user = request.user
            form.save()
            return redirect('reservation_details')

    form = ReservationForm(instance=reservation)
    context = {
        'form': form
    }
    return render(request, 'reservation_edit.html', context)


@login_required
def reservation_delete(request, res_id):
    reservation = get_object_or_404(Reservation, id=res_id)
    reservation.delete()

    return redirect('reservation_details')
