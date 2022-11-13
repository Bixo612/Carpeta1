from django.shortcuts import render
from .models import Persona

def inicio(request):
    return render(request, "index.html")

def respuesta(request):
    return render(request, "respuesta.html")

def listar(request):
    pe = Persona.objects.all()
    return render(request, "listar.html",{'personas':pe})

def registro(request):
    rut_p  = request.POST['rut']
    nombre_p = request.POST['nombre']
    correo_electronico_p = request.POST['email']
    direccion_p = request.POST['direccion']
    telefono_p = request.POST['telefono']
    contrasenna_p = request.POST['contrasenna']
    
    # Aqui se deben hacer las validaciones

    per = Persona.objects.create(rut = rut_p, nombre = nombre_p, correo_electronico = correo_electronico_p, direccion = direccion_p, contrasenna = contrasenna_p, telefono = telefono_p)    
    return render(request, "respuesta.html", {'msj':per})


