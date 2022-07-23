from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import path, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ReservationForm
from .models import Reservation


# Create form data instances

class AddReservationView(CreateView):

    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_create.html'
    success_url = '/reservation/details/'

    # Set reservation user to current logged in user
    def post(self, request):
        form = ReservationForm(request.POST)
        res = form.save(commit=False)
        res.user = request.user
        res.save()
        return redirect('reservation_details')


# Display a list of all reservations
class ReservationListView(ListView):

    model = Reservation
    template_name = 'reservation_details.html'

    # Get object data and return it
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['current'] = Reservation.objects.all()
        else:
            context['current'] = Reservation.objects.filter(user=self.request.user)
        return context


# Update selected reservation
class ReservationUpdateView(UpdateView):

    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_edit.html'
    success_url = '/reservation/details/'


# Delete selected reservation
class ReservationDeleteView(DeleteView):

    model = Reservation
    success_url = reverse_lazy('reservation_details')
