from django.db import models
from products.models import Product

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=255, default='Review')
    text = models.TextField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)