from django.shortcuts import render, redirect
from .models import Ventas

# Create your views here.
def inicio_vistaVenta(request):
    
    LasVentas = Ventas.objects.all()
    return render(request, "gestionarVenta.html", {"ElVentas": LasVentas})

def registrarVenta(request):
    Id_Ventas=request.POST["txtVentas"]
    Id_Producto=request.POST["txtProduc"]
    Id_Cliente=request.POST["txtCliente"]
    Metodo_pago=request.POST["txtPago"]
    Fecha_Venta=request.POST["txtFecha"]
    Id_empleado=request.POST["txtEmpleado"]
    Total=request.POST["txtTotal"]

    guardarVentas = Ventas.objects.create(
        Id_Ventas=Id_Ventas, Id_Producto=Id_Producto, Id_Cliente=Id_Cliente, Metodo_pago=Metodo_pago, Fecha_Venta=Fecha_Venta, Id_empleado=Id_empleado, Total=Total
    )

    return redirect("inicio_vistaVenta")

def seleccionarVenta(request, Id_Ventas):
    LasVentas = Ventas.objects.get(Id_Ventas=Id_Ventas)
    return render(request, "editarVenta.html", {"ElVentas": LasVentas})

def editarVenta(request):
    Id_Ventas=request.POST["txtVentas"]
    Id_Producto=request.POST["txtProduc"]
    Id_Cliente=request.POST["txtCliente"]
    Metodo_pago=request.POST["txtPago"]
    Fecha_Venta=request.POST["txtFecha"]
    Id_empleado=request.POST["txtEmpleado"]
    Total=request.POST["txtTotal"]
    
    ElVentas = Ventas.objects.get(Id_Ventas=Id_Ventas)
    ElVentas.Id_Producto = Id_Producto
    ElVentas.Id_Cliente = Id_Cliente
    ElVentas.Metodo_pago = Metodo_pago
    ElVentas.Fecha_Venta = Fecha_Venta
    ElVentas.Id_empleado = Id_empleado
    ElVentas.Total = Total
    ElVentas.save()

    return redirect("inicio_vistaVenta")

def borrarVenta(request, Id_Ventas):
    producto = Ventas.objects.get(Id_Ventas=Id_Ventas)
    producto.delete()
    return redirect("inicio_vistaVenta")
