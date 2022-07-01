from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Menu(models.Model):

    MENU_TYPE = (
        ('Starter', 'starter'),
        ('Main', 'main'),
        ('Desert', 'desert'),
    )

    type = models.CharField(max_length=10, choices=MENU_TYPE)
    name = models.CharField(max_length=50)
    description = models.TextField()
