from django.db import models

# Create your models here.

class Proveedor(models.Model):
    id_proveedor = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.SmallIntegerField()
    representante = models.CharField(max_length=100)
    tipo_pago = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre 