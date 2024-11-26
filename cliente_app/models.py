from django.db import models

# Create your models here.

class Clientes(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=100)
    fecha_n = models.DateTimeField()
    historial_c = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
