
from django.forms import ModelForm
from django import forms
from .models import Reservation
from datetime import datetime, timedelta

today = datetime.today()
strtoday = str(today)[:10]


class ReservationForm(ModelForm):
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

    # def clean(self):
    #     super(ReservationForm, self).clean()

    #     seats = self.cleaned_data.get('seats')

    #     if seats <= 0:
    #         self.errors['seats'] = self.error_class(['Pick a number of seats between 1 and 5'])

    #     return self.cleaned_data


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
