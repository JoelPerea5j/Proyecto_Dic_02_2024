from django.urls import path
from Ventas_app import views

urlpatterns = [
    path("inicio_vistaVenta", views.inicio_vistaVenta, name="inicio_vistaVenta"),
    path("registrarVenta/", views.registrarVenta, name="registrarVenta"),
    path("seleccionarVenta/<Id_Ventas>", views.seleccionarVenta, name="seleccionarVenta"),
    path("editarVenta/", views.editarVenta, name="editarVenta"),
    path("borrarVenta/<Id_Ventas>", views.borrarVenta, name="borrarVenta"),
]
