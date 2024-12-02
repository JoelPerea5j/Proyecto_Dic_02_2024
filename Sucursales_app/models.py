from django.db import models

# Create your models here.
class Sucursales(models.Model):
    Id_Sucursal=models.CharField(primary_key=True,max_length=6)
    Ubicacion=models.CharField(max_length=100)
    Telefono=models.CharField(max_length=100)
    Nombre=models.CharField(max_length=100)
    Horarios=models.CharField(max_length=100)
    Gerente=models.CharField(max_length=100)
    Administracion=models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre