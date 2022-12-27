from django.shortcuts import render
from msilib.schema import Error
from .models import Certificado

def inicio(request):
    return render(request,"index.html")

def ingresar(request):
    return render(request,"ingresar.html")

def registro(request):
    #realizar ingreso
    msj = None
    id_certificado_c = request.POST['id_certificado']
    nombre_c = request.POST['nombre']
    fecha_c = request.POST['fecha']
    curso_c = request.POST['curso']
    version_c = request.POST['version']
    id_verificacion_c = request.POST['id_validacion']
    
    try:
        Certificado.objects.create(id_certificado = id_certificado_c , nombre = nombre_c , fecha = fecha_c , curso = curso_c , version = version_c , id_verificacion = id_verificacion_c)
        msj = 'Se ha guardado el certificado'
    except Error as err:
        msj = f'ha ocurrido un problema en la operación_, {err}'

    return render(request,"respuesta.html",{'msj':msj})

def actualizar(request):
    return render(request,"actualizar.html")

def actualiza (request):
    #realizar actualizar
    cer = None
    msj = ""
    visible = ""
    try:
        cer = Certificado.objects.get(id_certificado = request.GET['txtValidador'])
        visible = "visible"
        return render(request,"actualizar.html",{'fomr2':visible,'cert':cer})
    except:
        cer = None
    
    if cer == None:
        id = None
        try:
            id = request.POST['id_certificado']
        except:
            id = None
        
        if id != None:
            cer = Certificado.objects.get(id_certificado = id)
            nombre_c = request.POST['nombre']
            fecha_c = request.POST['fecha']
            curso_c = request.POST['curso']
            version_c = request.POST['version']
            id_verificacion_c = request.POST['id_verificacion']

            cer.nombre = nombre_c
            cer.fecha = fecha_c
            cer.curso = curso_c
            cer.version = version_c
            cer.id_verificacion = id_verificacion_c

            try:
                cer.save()
                msj = "Se ha actualizado el cetificado"
            except:
                msj = "Ha ocurrido un error al actualizar el certificado"

            
            visible = "hidden"
            return render(request,"respuesta.html",{'msj':msj})
        
        else:
            msj = "No se ha encontrado el certificado"
            visibilidad = "hidden"
            return render(request, "actualizar.html", {"msj":msj, "form2":visibilidad})
    else:
        msj = "No se encontró el certificado solicitado"
        visibilidad = "hidden"
        return render(request, "actualizar.html", {"msj":msj, "form2":visibilidad})

def listar(request):
    cer = Certificado.objects.all()
    return render(request,"listar.html",{'certificados':cer})

def validar(request):
    return render(request,"validar.html")

def valida(request):
    #realizar valida
    msj = None
    id_certificado_c = request.POST['txtCertificado']
    id_verificacion_c = request.POST['txtValidador']
    try:
        cer = Certificado.objects.get(id_certificado = id_certificado_c)
        if cer.id_verificacion == id_verificacion_c:
            msj = "Certificado Valido"
            return render(request,"respuesta.html",{'msj':msj})
        else:
            msj = "Información no coincide"
            return render(request,"respuesta.html",{'msj':msj})
    except:
        msj = "Información no coincide"
        return render(request,"respuesta.html",{'msj':msj})

def eliminar(request):
    return render(request,"eliminar.html")

def elimina(request):
    #realizar elimina
    msj = None
    try:
        cer = Certificado.objects.get(id_certificado = request.POST['txtValidador'])
        cer.delete()
        msj = "Certificado Eliminado"
        return render(request,"respuesta.html",{'msj':msj})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'Certificado no existe'
        else:
            msj = 'Ha ocurrido un problema' 
        return render(request,"respuesta.html", {"msj":msj})    
