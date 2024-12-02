from django.shortcuts import render, redirect
from .models import Productos

# Create your views here.
def inicio_vistaProducto(request):
    losproductos = Productos.objects.all()
    return render(request, "gestionarProducto.html", {"misproductos": losproductos})

def registrarProducto(request):
    id_producto=request.POST["txtid_producto"]
    id_suculsal=request.POST["txtsucursal"]
    nombre_producto=request.POST["txtnom_pro"]
    precio=request.POST["numprecio"]
    marca=request.POST["txtmarca"]
    stock=request.POST["txtstock"]
    Tipo_produc=request.POST["txttipo_pro"]
    Fecha_creacion=request.POST["txtFecha"]

    guardarproducto = Productos.objects.create(
        id_producto=id_producto, id_suculsal=id_suculsal, nombre_producto=nombre_producto, precio=precio, marca=marca, stock=stock, Tipo_produc=Tipo_produc,
        Fecha_creacion=Fecha_creacion
    )

    return redirect("inicio_vistaProducto")

def seleccionarProducto(request, id_producto):
    losproductos = Productos.objects.get(id_producto=id_producto)
    return render(request, "editarProducto.html", {"misproductos": losproductos})

def editarProducto(request):
    id_producto=request.POST["txtid_producto"]
    id_suculsal=request.POST["txtsucursal"]
    nombre_producto=request.POST["txtnom_pro"]
    precio=request.POST["numprecio"]
    marca=request.POST["txtmarca"]
    stock=request.POST["txtstock"]
    Tipo_produc=request.POST["txttipo_pro"]
    Fecha_creacion=request.POST["txtFecha"]
    
    producto = Productos.objects.get(id_producto=id_producto)
    producto.id_suculsal = id_suculsal
    producto.precio = precio
    producto.nombre_producto = nombre_producto
    producto.precio = precio
    producto.marca = marca
    producto.stock = stock
    producto.Tipo_produc=Tipo_produc
    producto.Fecha_creacion = Fecha_creacion
    producto.save()

    return redirect("inicio_vistaProducto")

def borrarProducto(request, id_producto):
    producto = Productos.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("inicio_vistaProducto")
