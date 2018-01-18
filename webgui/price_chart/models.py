from django.db import models


class Transaction(models.Model):
    trading_par = models.CharField(max_length=6)
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=12, decimal_places=3)
    amount = models.DecimalField(max_digits=16, decimal_places=10)
    tid = models.PositiveIntegerField(primary_key=True)
