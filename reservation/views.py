from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import path, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ReservationForm
from .models import Reservation
from django.forms import ModelForm
from django import forms
from django.contrib.messages.views import SuccessMessageMixin


# Create form data instances

class AddReservationView(SuccessMessageMixin, CreateView):

    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_create_form.html'
    success_url = '/reservation/list/'
    success_message = 'Reservation created!'

    def get_context_data(self):
        context = super().get_context_data(**kwargs)

    # Set reservation user to current logged in user and ensure form is valid before save
    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        return super().form_valid(form)


# Display a list of all reservations
class ReservationListView(ListView):

    model = Reservation
    template_name = 'reservation_list.html'

    # Get object data and return it
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['current'] = Reservation.objects.all()
        else:
            context['current'] = Reservation.objects.filter(user=self.request.user)
        return context


# Update selected reservation
class ReservationUpdateView(SuccessMessageMixin, UpdateView):

    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_update.html'
    success_url = '/reservation/list/'
    success_message = 'Reservation updated!'


# Delete selected reservation
class ReservationDeleteView(SuccessMessageMixin, DeleteView):

    model = Reservation
    success_url = reverse_lazy('reservation_list')
