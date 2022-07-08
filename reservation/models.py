from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    phone = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.user.username


class Table(models.Model):
    seats = models.IntegerField(null=False, blank=False)
    reserved = models.BooleanField()

    def __str__(self):
        return str(self.id)


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    date_booked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
