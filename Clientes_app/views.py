from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.
def inicio_vistaCliente(request):
    LosClientes = Cliente.objects.all()
    return render(request, "gestionarCliente.html", {"elcliente": LosClientes})

def registrarCliente(request):
    Nombre=request.POST["txtNombre"]
    Apellidos=request.POST["txtApellido"]
    INE=request.POST["txtINE"]
    Domicilio=request.POST["txtDomicilio"]
    Fecha_Nacimiente=request.POST["txtFecha"]

    guardarproducto = Cliente.objects.create(
        Nombre=Nombre, Apellidos=Apellidos, INE=INE, Domicilio=Domicilio, Fecha_Nacimiente=Fecha_Nacimiente
    )

    return redirect("inicio_vistaCliente")

def seleccionarCliente(request, Nombre):
    LosClientes = Cliente.objects.get(Nombre=Nombre)
    return render(request, "editarCliente.html", {"elcliente": LosClientes})

def editarCliente(request):
    Nombre=request.POST["txtNombre"]
    Apellidos=request.POST["txtApellido"]
    INE=request.POST["txtINE"]
    Domicilio=request.POST["txtDomicilio"]
    Fecha_Nacimiente=request.POST["txtFecha"]
    
    producto = Cliente.objects.get(Nombre=Nombre)
    producto.Apellidos = Apellidos
    producto.INE = INE
    producto.Nombre = Nombre
    producto.Domicilio = Domicilio
    producto.Fecha_Nacimiente = Fecha_Nacimiente
    producto.save()

    return redirect("inicio_vistaCliente")

def borrarCliente(request, Nombre):
    producto = Cliente.objects.get(Nombre=Nombre)
    producto.delete()
    return redirect("inicio_vistaCliente")
