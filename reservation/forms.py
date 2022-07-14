
from django.forms import ModelForm
from django import forms
from .models import Reservation


class ReservationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    # seats = forms.TextInput(attrs={'class': 'form-control'})
    # date = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    # time = forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})

    class Meta:
        model = Reservation
        fields = ['seats', 'date', 'time']
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


    #     plaeholders = {
    #         'seats': 'Please enter party size',
    #         'date': 'dd/mm/yy',
    #         'time': '00:00',
    #     }

    #     self.fields['date'].widget.input_type = 'date'
    #     self.fields['time'].widget.input_type = 'time' 
