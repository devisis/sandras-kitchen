from django.test import TestCase
from .forms import ReservationForm


class TestReservationForm(TestCase):

    def test_reservation_name_is_required(self):
        form = ReservationForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_reservation_seats_is_required(self):
        form = ReservationForm({'seats': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('seats', form.errors.keys())
        self.assertEqual(form.errors['seats'][0], 'This field is required.')

    def test_reservation_date_is_required(self):
        form = ReservationForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_reservation_time_is_required(self):
        form = ReservationForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')
