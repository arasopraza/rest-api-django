from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=255)
  sku = models.CharField(max_length=255)
  category = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock = models.DecimalField(max_digits=10, decimal_places=2)
  location = models.CharField(max_length=255)
  is_available = models.BooleanField(default=False)