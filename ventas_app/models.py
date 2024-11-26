from django.db import models

# Create your models here.

class Ventas(models.Model):
    id_venta = models.CharField(primary_key=True, max_length=6)
    fecha = models.DateTimeField()
    cliente_a = models.CharField(max_length=100)
    vehiculo_v = models.CharField(max_length=100)
    precio_f = models.BigIntegerField()
    metodo_p = models.CharField(max_length=100)

    def __str__(self):
        return self.id_venta 