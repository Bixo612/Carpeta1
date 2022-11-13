from inspect import ArgSpec
from msilib.schema import Error
from sqlite3 import IntegrityError
from django.shortcuts import render
from .models import Persona

def inicio(request):
    return render(request,"index.html")

def respuesta(request):
    return render(request,"respuesta.html")

def listar(request):
    p = Persona.objects.all()
    return render(request,"listar.html",{'personas':p})

def registro(request):
    msj = None
    rut_p = request.POST['rut']
    nombre_p = request.POST['nombre']
    direccion_p = request.POST['direccion']
    contrasenna_p = request.POST['contrasenna']
    correo_p = request.POST['email']
    telefono_p = request.POST['telefono']

    # Aqui se deben hacer las validaciones
    try:
        Persona.objects.create(rut=rut_p,nombre=nombre_p,direccion=direccion_p,
                                contrasenna = contrasenna_p, correo_electronico = correo_p,
                                telefono = telefono_p)
        msj = 'se ha ingresado la persona'
    except Exception as ex:
        if str(ex.__cause__).find('EjemploORM_persona.rut') > 0:
            msj = 'ha ocurrido un problema en la operación, rut ya ingresado'
        elif str(ex.__cause__).find('EjemploORM_persona.correo_electronico') > 0:
            msj = 'ha ocurrido un problema en la operación, correo electrónico ya ingresado'
        else:
            'ha ocurrido un problema en la operación'
    except Error as err:
        msj = f'ha ocurrido un problema en la operación_, {err}'

    return render(request,"respuesta.html",{'msj':msj})

def ingresar(request):
    return render(request,"ingresar.html")

def actualizar(request):
    return render(request,"actualizar.html", {"form2":"hidden"})

def actualiza(request):
    per = None
    msj = ""
    visibilidad =""
    try:
        per = Persona.objects.get(rut = request.GET["rut_busqueda"])
        visibilidad = "visible"
        return render(request, "actualizar.html", {"form2":visibilidad, "p":per})
    except:
        per = None
    
    if per == None:
        rut = None
        try:
            rut = request.POST["rut"]
        except:
            rut = None

        if rut != None:
            per = Persona.objects.get(rut = rut)
            nombre = request.POST["nombre"]
            direccion = request.POST["direccion"]
            correoElectronico = request.POST["email"]
            contrasenna = request.POST["contrasenna"]
            telefono = request.POST["telefono"]

            per.nombre = nombre
            per.direccion = direccion
            per.contrasenna = contrasenna
            per.correo_electronico = correoElectronico
            per.telefono = telefono

            try:
                per.save()
                msj = "Se ha actualizado la persona"
            except:
                msj = "Se ha ocurrido un error al actualizar la persona"

            visibilidad = "hidden"
            return render(request, "actualizar.html", {"msj":msj, "form2":visibilidad})
        
        else:
            msj = "No se ha encontrado la persona"
            visibilidad = "hidden"
            return render(request, "actualizar.html", {"msj":msj, "form2":visibilidad})
    else:
        msj = "No se encontró la persona solicitada"
        visibilidad = "hidden"
        return render(request, "actualizar.html", {"msj":msj, "form2":visibilidad})
            
    
def eliminar(request):
    return render(request,"eliminar.html")       

    
def elimina(request):
    msj = None
    try:
        per = Persona.objects.get(rut = request.GET["rut_busqueda"])
        per.delete()
        msj = "Persona eliminada"
        return render(request, "eliminar.html",{"msj":msj})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'Rut no existe'
        else:
            msj = 'Ha ocurrido un problema'
        
        return render(request,"eliminar.html", {"msj":msj})    


