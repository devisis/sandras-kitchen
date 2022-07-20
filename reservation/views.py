from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import path, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ReservationForm
from .models import Reservation


class AddReservationView(CreateView):

    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_create.html'
    success_url = '/reservation/details/'

    # set reservation user to current logged in user
    def post(self, request):
        form = ReservationForm(request.POST)
        res = form.save(commit=False)
        res.user = request.user
        res.save()
        return redirect('reservation_details')


class ReservationListView(ListView):

    model = Reservation
    template_name = 'reservation_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReservationUpdateView(UpdateView):

    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_edit.html'
    success_url = '/reservation/details/'


class ReservationDeleteView(DeleteView):

    model = Reservation
    success_url = reverse_lazy('reservation_details')
