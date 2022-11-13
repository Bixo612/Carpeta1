from django.shortcuts import render
from .clases.eventos import Evento

def inicio(request):
    return render(request, 'inicio.html')

def formulario(request):
    return render(request, 'formulario.html')

def respuesta(request):
    nombre = request.POST['input_nombre']
    direccion = request.POST['input_direccion']
    correo = request.POST['input_correo']
    telefono = request.POST['input_telefono']
    fecha = request.POST['input_fecha']
    cantidad = request.POST['input_cantidad']
    ev = Evento(nombre,direccion,correo,telefono,fecha,cantidad)
    return render(request, 'respuesta.html',{"e":ev})