"""EjemploORM URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('respuesta', views.respuesta),
    path('registro', views.registro),
    path('listar', views.listar),
    path('actualizar', views.actualizar),
    path('actualiza', views.actualiza),
    path('elimina', views.elimina),
    path('eliminar', views.eliminar),
    path('ingresar',views.ingresar),
    ################################################################
    path('iniciar_sesion', views.iniciar_sesion),
    path('sesion',views.sesion)
]
