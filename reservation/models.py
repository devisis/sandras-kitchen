from django.db import models


class Reservation(models.Model):
    seats = models.IntegerField(null=False, blank=False)
    date = models.DateField()
    time = models.TimeField()
    date_booked = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)
