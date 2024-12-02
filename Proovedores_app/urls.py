from django.urls import path
from Proovedores_app import views

urlpatterns = [
    path("inicio_vistaProvedor", views.inicio_vistaProvedor, name="inicio_vistaProvedor"),
    path("registrarProvedor/", views.registrarProvedor, name="registrarProvedor"),
    path("seleccionarProvedor/<Id_compra>", views.seleccionarProvedor, name="seleccionarProvedor"),
    path("editarProvedor/", views.editarProvedor, name="editarProvedor"),
    path("borrarProvedor/<Id_compra>", views.borrarProvedor, name="borrarProvedor"),
]
