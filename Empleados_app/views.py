from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.
def inicio_vistaEmpleado(request):
    losempleados=Empleado.objects.all()
    return render(request,"gestionarEmpleado.html",{"misempleados":losempleados})

def registrarEmpleado(request):
    id_empleado=request.POST["txtid_empleado"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    salario=request.POST["numsalario"]
    fecha_nacimiento=request.POST["txtfecha"] 
    curp=request.POST["txtcurp"]
    RFC=request.POST["txtRFC"]
    
    guardarempleado=Empleado.objects.create(
        id_empleado=id_empleado, nombre=nombre, apellido=apellido, salario=salario, fecha_nacimiento=fecha_nacimiento,
        curp=curp, RFC=RFC
    )#Guarda el registro

    return redirect("inicio_vistaEmpleado")
def seleccionarEmpleado(request,id_empleado):
    losempleados=Empleado.objects.get(id_empleado=id_empleado)
    return render(request,"editarEmpleado.html", {"misempleados":losempleados})

def editarEmpleado(request):
    id_empleado=request.POST["txtid_empleado"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    salario=request.POST["numsalario"]
    fecha_nacimiento=request.POST["txtfecha"]
    curp=request.POST["txtcurp"]
    RFC=request.POST["txtRFC"]
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre=nombre
    empleado.apellido=apellido
    empleado.salario=salario
    empleado.apellido=apellido
    empleado.fecha_nacimiento=fecha_nacimiento
    empleado.curp=curp
    empleado.RFC=RFC
    empleado.save()#guarda registro actualizado
    return redirect("inicio_vistaEmpleado")

def borrarEmpleado(request, id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete() # borra el registro
    return redirect("inicio_vistaEmpleado")

    
