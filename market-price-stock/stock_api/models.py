from django.db import models
from django.utils import timezone


# Create your models here.
class StockPrice(models.Model):
    symbol = models.CharField(max_length=255)
    quantity = models.IntegerField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(default=timezone.now())
