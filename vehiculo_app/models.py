from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    id_vehiculo = models.CharField(primary_key=True, max_length=6)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.SmallIntegerField()
    estado = models.CharField(max_length=100)
    kilometraje = models.SmallIntegerField()

    def __str__(self):
        return self.modelo
    
