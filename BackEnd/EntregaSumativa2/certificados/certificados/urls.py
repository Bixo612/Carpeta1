"""certificados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
    path('', views.inicio),
    path('inicio', views.inicio),
    path('ingresar', views.ingresar),
    path('actualizar', views.actualizar),
    path('listar', views.listar),
    path('validar', views.validar),
    path('actualiza', views.actualiza),
    path('eliminar', views.eliminar),
    path('valida', views.valida),
    path('elimina', views.elimina),
    path('registro', views.registro),   
]
