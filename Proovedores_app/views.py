from django.shortcuts import render, redirect
from .models import Provedores

# Create your views here.
def inicio_vistaProvedor(request):
    LosProvedores = Provedores.objects.all()
    return render(request, "gestionarProvedor.html", {"misprovedores": LosProvedores})

def registrarProvedor(request):
    Id_compra=request.POST["txtCompra"]
    Nombre=request.POST["txtNombre"]
    Direccion=request.POST["txtDireccion"]
    Telefono=request.POST["txtTelefono"]
    Correo=request.POST["txtCorreo"]

    guardarproducto = Provedores.objects.create(
        Id_compra=Id_compra, Nombre=Nombre, Direccion=Direccion, Telefono=Telefono, Correo=Correo
    )

    return redirect("inicio_vistaProvedor")

def seleccionarProvedor(request, Id_compra):
    LosProvedores = Provedores.objects.get(Id_compra=Id_compra)
    return render(request, "editarProvedor.html", {"misprovedores": LosProvedores})

def editarProvedor(request):
    Id_compra=request.POST["txtCompra"]
    Nombre=request.POST["txtNombre"]
    Direccion=request.POST["txtDireccion"]
    Telefono=request.POST["txtTelefono"]
    Correo=request.POST["txtCorreo"]

    producto = Provedores.objects.get(Id_compra=Id_compra)
    producto.Nombre = Nombre
    producto.Direccion = Direccion
    producto.Telefono = Telefono
    producto.Correo = Correo
    producto.save()

    return redirect("inicio_vistaProvedor")

def borrarProvedor(request, Id_compra):
    producto = Provedores.objects.get(Id_compra=Id_compra)
    producto.delete()
    return redirect("inicio_vistaProvedor")
