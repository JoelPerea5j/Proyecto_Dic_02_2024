from django.urls import path
from Clientes_app import views

urlpatterns = [
    path("inicio_vistaCliente", views.inicio_vistaCliente, name="inicio_vistaCliente"),
    path("registrarCliente/", views.registrarCliente, name="registrarCliente"),
    path("seleccionarCliente/<Nombre>", views.seleccionarCliente, name="seleccionarCliente"),
    path("editarCliente/", views.editarCliente, name="editarCliente"),
    path("borrarCliente/<Nombre>", views.borrarCliente, name="borrarCliente"),
]
