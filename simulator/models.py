from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import yfinance as yf

class Positions(models.Model):
    stock = models.CharField(max_length=10)
    shares = models.TextField()
    boughtPrice = models.TextField()
    currentPrice = models.TextField()
    marketValue = models.TextField()
    change = models.TextField()
    date_bought = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.stock

class StockForm(models.Model): 
    stock = models.CharField(max_length=10)

    def __str__(self):
        return self.stock

    # NNOTE
    # Store $100,000 in user account