from django.db import models

# Create your models here.
class Provedores(models.Model):
    Id_compra=models.CharField(primary_key=True,max_length=6)
    Nombre=models.CharField(max_length=100)
    Direccion=models.CharField(max_length=100)
    Telefono=models.CharField(max_length=100)
    Correo=models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre