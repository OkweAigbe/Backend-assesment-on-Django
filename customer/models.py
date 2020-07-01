from django.db import models

# models here.

class Customer(models.Model):
    full_name       = models.CharField(max_length=50)
    email           = models.CharField(max_length=10)
    date_of_birth   = models.DateField()
    address         = models.CharField(max_length=50)

