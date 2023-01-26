from django.shortcuts import render
from msilib.schema import Error
from .models import Juego, Pelicula, Libro, Disco, Vinilo, Genero

def irInicio(request):
    return render(request, "inicio.html")

def irRegistro(request):
    gen = Genero.objects.all()
    return render(request, "registro.html", {'generos': gen,'alerts': False})

def irCategorias(request):
    gen = Genero.objects.all()
    return render(request, "categorias.html", {'generos': gen})


def irLista(request):
    p = Pelicula.objects.all()
    j = Juego.objects.all()
    l = Libro.objects.all()
    d = Disco.objects.all()
    v = Vinilo.objects.all()
    return render(request, "lista.html", {'juegos': j, 'peliculas': p, 'libros': l, 'discos': d, 'vinilos': v})

def fx_registrarJuego(request):
    msj = None
    j_id = 'J' + request.POST['txt_j_id']
    j_nombre = request.POST['txt_j_nombre']
    j_consola = request.POST['txt_j_consola']
    j_genero = request.POST['txt_j_genero']
    j_ano = request.POST['txt_j_ano']
    j_clasificacion = request.POST['txt_j_clasificacion']
    try:
        Juego.objects.create(
            idJuego=j_id, nombre=j_nombre,
            consola=j_consola, genero=j_genero,
            an_o=j_ano, clasificacion=j_clasificacion,
            disponible=True)
        msj = "Juego " + str(j_id) + " registrado correctamente"
    except Error as err:
        msj = f'\n Ha ocurrido un error en la operacion {err}'
    return render(request, "registro.html", {'msj': msj,'alert': True})

def fx_registrarPelicula(request):
    msj = None
    p_id = 'P' + request.POST['txt_p_id']
    p_nombre = request.POST['txt_p_nombre']
    p_genero = request.POST['txt_p_genero']
    p_ano = request.POST['txt_p_ano']
    p_clasificacion = request.POST['txt_p_clasificacion']
    p_director = request.POST['txt_p_director']
    p_duracion = request.POST['txt_p_duracion']
    try:
        Pelicula.objects.create(
            idPelicula=p_id, nombre=p_nombre,
            director=p_director, genero=p_genero,
            an_o=p_ano, clasificacion=p_clasificacion,
            duracion=p_duracion, disponible=True)
        msj = "Pelicula " + str(p_id) + " registrado correctamente"
    except Error as err:
        msj = f'\n Ha ocurrido un error en la operacion {err}'
    return render(request, "registro.html", {'msj': msj,'alert': True})

def fx_registrarLibro(request):
    msj = None
    l_id = 'L' + request.POST['txt_l_id']
    l_nombre = request.POST['txt_l_nombre']
    l_genero = request.POST['txt_l_genero']
    l_ano = request.POST['txt_l_ano']
    l_escritor = request.POST['txt_l_escritor']
    l_editorial = request.POST['txt_l_editorial']
    try:
        Libro.objects.create(
            idLibro=l_id, nombre=l_nombre,
            escritor=l_escritor, genero=l_genero,
            an_o=l_ano, editorial=l_editorial)
        msj = "Libro " + str(l_id) + " registrado correctamente"
    except Error as err:
        msj = f'\n Ha ocurrido un error en la operacion {err}'
    return render(request, "registro.html", {'msj': msj,'alert': True})

def fx_registrarDisco(request):
    msj = None
    d_id = 'D' + request.POST['txt_d_id']
    d_nombre = request.POST['txt_d_nombre']
    d_genero = request.POST['txt_d_genero']
    d_ano = request.POST['txt_d_ano']
    d_interprete = request.POST['txt_d_interprete']
    d_duracion = request.POST['txt_d_duracion']
    try:
        Disco.objects.create(
            idDisco=d_id, nombre=d_nombre,
            genero=d_genero, an_o=d_ano,
            interprete=d_interprete, duracion=d_duracion,
            disponible=True
        )
        msj = "Disco " + str(d_id) + " registrado correctamente"
    except Error as err:
        msj = f'\n Ha ocurrido un error en la operacion {err}'
    return render(request, "registro.html", {'msj': msj,'alert': True})

def fx_registrarVinilo(request):
    msj = None
    v_id = 'V' + request.POST['txt_v_id']
    v_nombre = request.POST['txt_v_nombre']
    v_genero = request.POST['txt_v_genero']
    v_ano = request.POST['txt_v_ano']
    v_interprete = request.POST['txt_v_interprete']
    v_duracion = request.POST['txt_v_duracion']
    try:
        Vinilo.objects.create(
            idVinilo=v_id, nombre=v_nombre,
            genero=v_genero, an_o=v_ano,
            interprete=v_interprete, duracion=v_duracion,
            disponible=True
        )
        msj = "Vinilo " + str(v_id) + " registrado correctamente"
    except Error as err:
        msj = f'\n Ha ocurrido un error en la operacion {err}'
    return render(request, "registro.html", {'msj': msj,'alert': True}) 

def fx_registarGenero(request):
    gen = Genero.objects.all()
    msj = None
    g_idG = request.POST['txt_g_id']
    g_genero = request.POST['txt_g_genero']
    g_tipo = request.POST['txt_g_tipo']
    try:
        Genero.objects.create(
            idG=g_idG,
            genero=g_genero,
            tipo=g_tipo
        )
        msj = "Genero " + str(g_idG) + " registrado correctamente"
    except Error as err:
        msj = f'\n Ha ocurrido un error en la operacion {err}'
    return render(request, "categorias.html", {'generos': gen, 'msj': msj})

def fx_eliminarGenero(request):
    msj = None
    gen = Genero.objects.all()
    try:
        ge = Genero.objects.get(idG=request.GET['f_g_id'])
        ge.delete()
        msj = 'Genero eliminado correctamente'
        return render(request, "categorias.html", {'generos': gen, "msj": msj})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'Genero no existe'
        else:
            msj = 'Ha ocurrido un problema'
        return render(request, "categorias.html", {'generos': gen, "msj": msj})

def fx_eliminarJuego(request):
    msj = None
    try:
        ju = Juego.objects.get(idJuego=request.GET['txt_j_id'])
        ju.delete()
        msj = 'Juego eliminado'
        return render(request, "inicio.html", {'msj': msj})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'Juego no existe'
        else:
            msj = 'Ha ocurrido un problema'
        return render(request, "eliminar.html", {"msj": msj})

def fx_eliminarPelicula(request):
    msj = None
    try:
        pe = Pelicula.objects.get(idPelicula=request.GET['txt_p_id'])
        pe.delete()
        msj = 'Pelicula eliminada'
        return render(request, "eliminar.html", {'msj': msj})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'Pelicula no existe'
        else:
            msj = 'Ha ocurrido un problema'
        return render(request, "eliminar.html", {"msj": msj})

def fx_eliminarlibro(request):
    msj = None
    try:
        li = Libro.objects.get(idLibro=request.GET['txt_l_id'])
        li.delete()
        msj = 'Libro eliminado'
        return render(request, "eliminar.html", {'msj': msj})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'Libro no existe'
        else:
            msj = 'Ha ocurrido un problema'
        return render(request, "inicio.html", {"msj": msj})

def fx_actualizar(request):
    gen = Genero.objects.all()
    msj = None
    try:
        cat = request.GET["select_categoria"]
        if cat == "J":
            cont = Juego.objects.get(idJuego=request.GET["txt_id_actualizar"])
            return render(request, "actualizar.html", {'contenido': cont, 'vista': 'J', 'generos': gen})
        elif cat == "P":
            cont = Pelicula.objects.get(
                idPelicula=request.GET["txt_id_actualizar"])
            return render(request, "actualizar.html", {'contenido': cont, 'vista': 'P', 'generos': gen})
        elif cat == "L":
            cont = Libro.objects.get(idLibro=request.GET["txt_id_actualizar"])
            return render(request, "actualizar.html", {'contenido': cont, 'vista': 'L', 'generos': gen})
        else:
            msj = "Categoria no selecionada"
            return render(request, "actualizar.html", {'msj': msj})
    except:
        msj = "Contenido no encontrado"
        return render(request, "actualizar.html", {'msj': msj})

def fx_buscar(request):
    msj = None
    id = request.POST['txt_id']
    id = id.upper()
    if id[0] == 'L':
        try:
            cont = Libro.objects.get(id)
        except:
            return render(request, "inicio.html")
        return render(request, 'buscar.html')
    elif id[0] == 'P':
        return render(request, 'buscar.html')
    elif id[0] == 'J':
        return render(request, 'buscar.html')
    elif id[0] == 'D':
        return render(request, 'buscar.html')
    elif id[0] == 'V':
        return render(request, 'buscar.html')
    else:
        return render(request, "inicio.html")
