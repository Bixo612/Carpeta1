"""evaluacion1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio),
    path('forumalrio_reserva',views.to_formularioReserva),
    path('reservar',views.fx_reservar),
    path('respuesta_listado',views.to_listado),
    path('formulario_eliminar',views.to_formularioEliminar),
    path('eliminar',views.fx_eliminar),
    path('formulario_confirmar',views.to_formularioConfirmar),
    path('confirmar',views.fx_confirmarId),
    path('actualizar',views.fx_actualizar),
    path('formulario_busqueda',views.to_formularioBusqueda),
    path('buscar',views.fx_buscar),
]
