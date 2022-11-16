from inspect import ArgSpec
from msilib.schema import Error
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from .models import Persona

def inicio(request):
    sesion = None
    try:
        sesion = request.session['sesion_activa']
        if sesion != 'Activa':
            sesion = None
    except:
        sesion = None
    return render(request,"index.html",{'sesion_activa':sesion})
    

def respuesta(request):
    sesion = None
    try:
        sesion = request.session['sesion_activa']
    except:
        return render(request,"iniciar_sesion.html")
    return render(request,"respuesta.html",{'sesion_activa':sesion})

def listar(request):
    sesion = None
    try:
        sesion = request.session['sesion_activa']
    except:
        return render(request,"iniciar_sesion.html")
    p = Persona.objects.all()
    return render(request,"listar.html",{'sesion_activa':sesion, "personas":p})

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
    sesion = None
    try:
        sesion = request.session['sesion_activa']
        return render(request,"ingresar.html",{'sesion_activa':sesion})
    except:
        return render(request,"ingresar.html",{'sesion_activa':sesion})

def actualizar(request):
    sesion = None
    try:
        sesion = request.session['sesion_activa']
    except:
        return render(request,"iniciar_sesion.html")
    return render(request,"actualizar.html",{'sesion_activa':sesion,"form2":"hidden"})

def actualiza(request):
    try:
        sesion = request.session['sesion_activa']
    except:
        return render(request,"iniciar_sesion.html")
    per = None
    msj = ""
    visibilidad =""
    try:
        per = Persona.objects.get(rut = request.GET["rut_busqueda"])
        visibilidad = "visible"
        return render(request, "actualizar.html", {"form2":visibilidad, "p":per,'sesion_activa':sesion})
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
            return render(request, "actualizar.html", {"msj":msj, "form2":visibilidad,'sesion_activa':sesion,})
        
        else:
            msj = "No se ha encontrado la persona"
            visibilidad = "hidden"
            return render(request, "actualizar.html", {"msj":msj, "form2":visibilidad,'sesion_activa':sesion,})
    else:
        msj = "No se encontró la persona solicitada"
        visibilidad = "hidden"
        return render(request, "actualizar.html", {"msj":msj, "form2":visibilidad,'sesion_activa':sesion,})
            
    
def eliminar(request):
    sesion = None
    try:
        sesion = request.session['sesion_activa']
    except:
        return render(request,"iniciar_sesion.html",{'sesion_activa':sesion})
    return render(request,"eliminar.html",{'sesion_activa':sesion})       

    
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

def iniciar_sesion(request):
    try:
        if request.session['sesion_activa'] == 'Activa':
            del request.session['sesion_activa']
            return render(request,"index.html")
        else:
            return render(request,"iniciar_sesion.html")
    except:
        return render(request,"iniciar_sesion.html")

def sesion(request):
    per = None
    try:
        per = Persona.objects.get(rut = request.POST["rut"])
        if(per.contrasenna == request.POST["contrasenna"]):
            request.session["sesion_activa"] = "Activa"
            return redirect(inicio)
        else:
            return render(request,"iniciar_sesion.html", {"mensaje":"contraseña no válida"})
    except Exception as ex:
        return render(request,"iniciar_sesion.html", {"mensaje":ex})

