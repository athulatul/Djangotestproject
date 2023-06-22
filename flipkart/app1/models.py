from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=25, decimal_places=8)
    description = models.CharField(max_length=500)





