from django.shortcuts import render, redirect
from .models import Sucursales

# Create your views here.
def inicio_vistaSucursal(request):
    LasSucursales = Sucursales.objects.all()
    return render(request, "gestionarSucursal.html", {"sucursales": LasSucursales})

def registrarSucursal(request):
    Id_Sucursal=request.POST["txtSucursal"]
    Ubicacion=request.POST["txtUbi"]
    Telefono=request.POST["txtTelefono"]
    Nombre=request.POST["txtnombre"]
    Horarios=request.POST["txtHorarios"]
    Gerente=request.POST["txtGerente"]
    Administracion=request.POST["txtAdmin"]

    guardarproducto = Sucursales.objects.create(
        Id_Sucursal=Id_Sucursal, Ubicacion=Ubicacion, Telefono=Telefono, Nombre=Nombre, Horarios=Horarios, Gerente=Gerente, Administracion=Administracion
    )

    return redirect("inicio_vistaSucursal")

def seleccionarSucursal(request, Id_Sucursal):
    LasSucursales = Sucursales.objects.get(Id_Sucursal=Id_Sucursal)
    return render(request, "editarSucursal.html", {"sucursales": LasSucursales})

def editarSucursal(request):
    Id_Sucursal=request.POST["txtSucursal"]
    Ubicacion=request.POST["txtUbi"]
    Telefono=request.POST["txtTelefono"]
    Nombre=request.POST["txtnombre"]
    Horarios=request.POST["txtHorarios"]
    Gerente=request.POST["txtGerente"]
    Administracion=request.POST["txtAdmin"]
    
    producto = Sucursales.objects.get(Id_Sucursal=Id_Sucursal)
    producto.Ubicacion = Ubicacion
    producto.Telefono = Telefono
    producto.Nombre = Nombre
    producto.Horarios = Horarios
    producto.Gerente = Gerente
    producto.Administracion = Administracion
    producto.save()

    return redirect("inicio_vistaSucursal")

def borrarSucursal(request, Id_Sucursal):
    producto = Sucursales.objects.get(Id_Sucursal=Id_Sucursal)
    producto.delete()
    return redirect("inicio_vistaSucursal")
