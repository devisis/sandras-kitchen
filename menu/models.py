from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):

    # defining menu types
    MENU_TYPE = (
        ('Starter', 'starter'),
        ('Main', 'main'),
        ('Dessert', 'dessert'),
    )

    type = models.CharField(max_length=10, choices=MENU_TYPE)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return str(self.name)
