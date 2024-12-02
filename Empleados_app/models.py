from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    salario= models.IntegerField(default=100)
    fecha_nacimiento=models.CharField(max_length=100)
    curp=models.CharField(max_length=100)
    RFC= models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre