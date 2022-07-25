from django.db import models
from django.db.models import IntegerField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# define models with their constraints
class Reservation(models.Model):
    seats = models.IntegerField(
        null=False,
        blank=False,
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
            ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, null=True)
    date = models.DateField()
    time = models.TimeField()
    date_booked = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)
