from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.

class Vehiculo(models.Model):
    marca= models.CharField(max_length= 20)
    patente = models.CharField(max_length= 8)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    tipo = models.CharField(max_length= 20)


