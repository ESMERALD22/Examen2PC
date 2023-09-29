from django.db import models


class Ordenes(models.Model):
    nombreCliente = models.CharField(max_length=50) 
    total = models.DecimalField(max_digits=10, decimal_places=2)
