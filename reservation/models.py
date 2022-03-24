from django.db import models

# Create your models here.


class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=25, null=False, blank=False)
    surname = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.email
