from django.db import models

# Create your models here.
class Productos(models.Model):
    id_producto=models.CharField(primary_key=True,max_length=6)
    id_suculsal=models.CharField(max_length=100)
    nombre_producto=models.CharField(max_length=100)
    precio=models.IntegerField()
    marca=models.CharField(max_length=100)
    stock=models.CharField(max_length=100)
    Tipo_produc=models.CharField(max_length=100)
    Fecha_creacion=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_producto