from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, null=True)
    seats = models.IntegerField(null=False, blank=False)
    date = models.DateField()
    time = models.TimeField()
    date_booked = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)
