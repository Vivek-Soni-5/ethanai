from django.db import models

# Create your models here.

class Financial(models.Model):
    ISIN = models.CharField(max_length=150)
    symbol = models.CharField(max_length=150)
    date = models.CharField(max_length=150, null=True)
    asset_class = models.CharField(max_length=150)
    quantity = models.IntegerField(null=True)
    market_price = models.IntegerField(null=True)
    cost_price = models.IntegerField(null=True)
    
