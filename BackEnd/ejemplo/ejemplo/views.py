from django.shortcuts import render
from .clases.personas import Persona

def inicio(request):
    return render(request, 'index.html')

def formulario(request):
    return render(request, 'formulario.html')

def respuesta(request):
    nombre =  request.GET["txtnombre"]
    direccion = request.GET["txtdireccion"]
    per = Persona(nombre,direccion)
    return render(request, 'respuesta.html',{"p":per})
