from django.urls import path
from .views import vistaVehiculos,vistaInsumosComputacionales,vistaArticuloOficina

urlpatterns = [
    path('vehiculos',vistaVehiculos.as_view(),name="listaVehiculos"),
    path('insumosComputacionales',vistaInsumosComputacionales.as_view(),name="listaInsumosComputacionales"),
    path('articulo',vistaArticuloOficina.as_view(),name="listaArticulo"),
]