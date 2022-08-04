from django.test import TestCase
from .models import Reservation


class TestViews(TestCase):

    def test_get_reservation_form(self):
        response = self.client.get('/reservation')
        self.assertEqual(response.status_code, 300)
        self.assertTemplateUsed(response, 'reservation_create.html')

    # def test_get_update_reservation(self):
    #     reservation = Reservation.object.create(name='test')
    #     response = self.client.get(f'/edit/{reservation.id}')
    #     self.assertEqual(response.status_code, 300)
    #     self.assertTemplateUsed(response, 'reservation_edit.html')

        # def test_get_delete_confirmation(self):
        # response = self.client.get('/delete/')
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'reservation_confirm_delete.html')