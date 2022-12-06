"""BlockBuster URL Configuration

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
#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.irInicio),
    #url de redireccion
    path('Inicio', views.irInicio),
    path('Registro', views.irRegistro),
    path('Lista', views.irLista),
    path('Eliminar', views.irEliminar),
    path('Actualizar',views.irActualizar),
    #url de funciones
    path('registar_juego', views.fx_registrarJuego),
    path('registar_pelicula',views.fx_registrarPelicula),
    path('registar_libro',views.fx_registrarLibro),
    path('fx_eliminar_juego', views.fx_eliminarJuego),
    path('fx_eliminar_pelicula', views.fx_eliminarPelicula),
    path('fx_eliminar_libro', views.fx_eliminarlibro),
]