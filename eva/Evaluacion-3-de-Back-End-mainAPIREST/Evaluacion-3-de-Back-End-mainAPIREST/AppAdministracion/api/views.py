from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from AppAdministracion.models import Vehiculo,InsumoComputacional,ArticuloOficina

# Create your views here.

class vistaVehiculos(View):
    def get(self, request):
        vehiculos = list(Vehiculo.objects.values())
        datos = {'mensaje':"Success",'vehiculos':vehiculos}
        return JsonResponse(datos)


class vistaInsumosComputacionales(View):
    def get(self, request):
        insumos = list(InsumoComputacional.objects.values())
        datos = {'mensaje':"Success",'insumos':insumos}
        return JsonResponse(datos)


class vistaArticuloOficina(View):
    def get(self, request):
        articulo = list(ArticuloOficina.objects.values())
        datos = {'mensaje':"Success",'articulo':articulo}
        return JsonResponse(datos)


