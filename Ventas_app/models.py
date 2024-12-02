from django.db import models

# Create your models here.
class Ventas(models.Model):
    Id_Ventas=models.CharField(primary_key=True,max_length=6)
    Id_Producto=models.CharField(max_length=100)
    Id_Cliente=models.CharField(max_length=100)
    Metodo_pago=models.CharField(max_length=100)
    Fecha_Venta=models.CharField(max_length=100)
    Id_empleado=models.CharField(max_length=100)
    Total=models.CharField(max_length=100)

    def __str__(self):
        return self.Id_Producto