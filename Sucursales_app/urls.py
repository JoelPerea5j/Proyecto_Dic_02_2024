from django.urls import path
from Sucursales_app import views

urlpatterns = [
    path("inicio_vistaSucursal", views.inicio_vistaSucursal, name="inicio_vistaSucursal"),
    path("registrarSucursal/", views.registrarSucursal, name="registrarSucursal"),
    path("seleccionarSucursal/<Id_Sucursal>", views.seleccionarSucursal, name="seleccionarSucursal"),
    path("editarSucursal/", views.editarSucursal, name="editarSucursal"),
    path("borrarSucursal/<Id_Sucursal>", views.borrarSucursal, name="borrarSucursal"),
]
