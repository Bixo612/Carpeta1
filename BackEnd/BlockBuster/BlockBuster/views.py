from django.shortcuts import render
from msilib.schema import Error
from .models import Juego
from .models import Pelicula

def irInicio(request):
    return render(request, "inicio.html")

def irRegistro(request):
    return render(request, "registro.html")

def irEliminar(request):
    return render(request, "eliminar.html")

def irLista(request):
    p = Pelicula.objects.all()
    j = Juego.objects.all()
    return render(request, "lista.html", {'juegos': j, 'peliculas': p})

def fx_registrarJuego(request):
    msj = None
    j_id = request.POST['txt_j_id']
    j_nombre = request.POST['txt_j_nombre']
    j_consola = request.POST['txt_j_consola']
    j_genero = request.POST['txt_j_genero']
    j_ano = request.POST['txt_j_ano']
    j_clasificacion = request.POST['txt_j_clasificacion']
    #
    try:
        Juego.objects.create(
            idJuego=j_id, nombre=j_nombre,
            consola=j_consola, genero=j_genero,
            an_o=j_ano, clasificacion=j_clasificacion)
        msj = "Juego " + str(j_id) + " registrado correctamente"
    except Error as err:
        msj = 'Ha ocurrido un error en la operacion' + err
    return render(request, "inicio.html", {'msj': msj})

def fx_registrarPelicula(request):
    msj = None
    p_id = request.POST['txt_p_id']
    p_nombre = request.POST['txt_p_nombre']
    p_director = request.POST['txt_p_director']
    p_genero = request.POST['txt_p_genero']
    p_ano = request.POST['txt_p_ano']
    p_clasificacion = request.POST['txt_p_clasificacion']
    #
    try:
        Pelicula.objects.create(
            idPelicula=p_id, nombre=p_nombre,
            director=p_director, genero=p_genero,
            an_o=p_ano, clasificacion=p_clasificacion)
        msj = "Pelicula " + str(p_id) + " registrado correctamente"
    except Error as err:
        msj = f'\n Ha ocurrido un error en la operacion'
    return render(request, "inicio.html", {'msj': msj})

def fx_eliminarJuego(request):
    msj = None
    try:
        ju = Juego.objects.get(id_j = request.GET['txt_j_id'])
        ju.delete()
        msj = 'Juego eliminado'
        return render(request, "inicio.html", {'msj': msj})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'juego no existe'
        else:
            msj = 'Ha ocurrido un problema'     
        return render(request,"inicio.html", {"msj":msj}) 

'''
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
'''