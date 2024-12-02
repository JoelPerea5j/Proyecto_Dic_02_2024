from django.db import models

# Create your models here.
class Cliente(models.Model):
    Nombre=models.CharField(primary_key=True,max_length=6)
    Apellidos=models.CharField(max_length=100)
    INE=models.CharField(max_length=100)
    Domicilio=models.CharField(max_length=100)
    Fecha_Nacimiente=models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre