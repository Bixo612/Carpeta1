from django.shortcuts import render
from msilib.schema import Error
from .models import Juego
from .models import Pelicula


def irInicio(request):
    return render(request, "inicio.html")


def irRegistro(request):
    return render(request, "registro.html")


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
        msj = f'\n Ha ocurrido un error en la operacion'
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
        msj = '''<div class="alert alert-warning alert-dismissible fade show" role="alert">
    <strong>Holy guacamole!</strong> You should check in on some of those fields below.
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>'''
    except Error as err:
        msj = f'\n Ha ocurrido un error en la operacion'
    return render(request, "inicio.html", {'msj': msj})
