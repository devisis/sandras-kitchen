
from django.forms import ModelForm
from django import forms
from .models import Reservation


class ReservationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Reservation
        fields = ['name', 'seats', 'date', 'time']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',
                    }
            ),
            'time': forms.TimeInput(
                format=('%H:%M'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a time',
                    'type': 'time',
                    }

            ),
        }


class EditReservations(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'seats', 'date', 'time']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',
                    }
            ),
            'time': forms.TimeInput(
                format=('%H:%M'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a time',
                    'type': 'time',
                    }

            ),
        }
