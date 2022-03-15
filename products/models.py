from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    desciption = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory_quantity = models.IntegerField()

# Create your models here.
