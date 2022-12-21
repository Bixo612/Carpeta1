from django.shortcuts import render
from msilib.schema import Error
from .models import Juego
from .models import Pelicula
from .models import Libro
from .models import Genero

def irInicio(request):
    return render(request, "inicio.html")

def irRegistro(request):
    gen = Genero.objects.all()
    return render(request, "registro.html",{'generos': gen})

def irEliminar(request):
    return render(request, "eliminar.html")

def irActualizar(request):
    return render(request, "actualizar.html")

def irCategorias(request):
    gen = Genero.objects.all()
    return render(request, "categorias.html",{'generos': gen}) 

def irLista(request):
    p = Pelicula.objects.all()
    j = Juego.objects.all()
    l = Libro.objects.all()
    return render(request, "lista.html", {'juegos': j, 'peliculas': p, 'libros': l})

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
            an_o=j_ano, clasificacion=j_clasificacion)
        msj = "Juego " + str(j_id) + " registrado correctamente"
    except Error as err:
        msj = f'\n Ha ocurrido un error en la operacion {err}'
    return render(request, "inicio.html", {'msj': msj})

def fx_registrarPelicula(request):
    msj = None
    p_id = 'P' + request.POST['txt_p_id']
    p_nombre = request.POST['txt_p_nombre']
    p_director = request.POST['txt_p_director']
    p_genero = request.POST['txt_p_genero']
    p_ano = request.POST['txt_p_ano']
    p_clasificacion = request.POST['txt_p_clasificacion']
    try:
        Pelicula.objects.create(
            idPelicula=p_id, nombre=p_nombre,
            director=p_director, genero=p_genero,
            an_o=p_ano, clasificacion=p_clasificacion)
        msj = "Pelicula " + str(p_id) + " registrado correctamente"
    except Error as err:
        msj = f'\n Ha ocurrido un error en la operacion {err}'
    return render(request, "registro.html", {'msj': msj})

def fx_registrarLibro(request):
    msj = None
    l_id = 'L' + request.POST['txt_l_id']
    l_nombre = request.POST['txt_l_nombre']
    l_escritor = request.POST['txt_l_escritor']
    l_genero = request.POST['txt_l_genero']
    l_ano = request.POST['txt_l_ano']
    l_clasificacion = request.POST['txt_l_clasificacion']
    try:
        Libro.objects.create(
            idLibro=l_id, nombre=l_nombre,
            escritor=l_escritor, genero=l_genero,
            an_o=l_ano, clasificacion=l_clasificacion)
        msj = "Libro " + str(l_id) + " registrado correctamente"
    except Error as err:
        msj = f'\n Ha ocurrido un error en la operacion {err}'
    return render(request, "registro.html", {'msj': msj})
    
def fx_registarGenero(request):
    gen = Genero.objects.all()
    msj = None
    g_idG     = request.POST['txt_g_id']
    g_genero  = request.POST['txt_g_genero']
    g_tipo    = request.POST['txt_g_tipo']
    try:
        Genero.objects.create(
            idG = g_idG,
            genero = g_genero,
            tipo = g_tipo
        )
        msj = "Genero " + str(g_idG) + " registrado correctamente"
    except Error as err:
        msj = f'\n Ha ocurrido un error en la operacion {err}'
    return render(request, "categorias.html", {'generos': gen,'msj': msj})

def fx_eliminarGenero(request):
    msj = None
    gen = Genero.objects.all()
    try:
        ge = Genero.objects.get(idG = request.GET['f_g_id'])
        ge.delete()
        msj = 'Genero eliminado correctamente'
        return render(request,"categorias.html", {'generos': gen,"msj":msj}) 
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'Genero no existe'
        else:
            msj = 'Ha ocurrido un problema'  
        return render(request,"categorias.html", {'generos': gen,"msj":msj}) 

def fx_eliminarJuego(request):
    msj = None
    try:
        ju = Juego.objects.get(idJuego = request.GET['txt_j_id'])
        ju.delete()
        msj = 'Juego eliminado'
        return render(request, "inicio.html", {'msj': msj})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'Juego no existe'
        else:
            msj = 'Ha ocurrido un problema'  
        return render(request,"eliminar.html", {"msj":msj}) 

def fx_eliminarPelicula(request):
    msj = None
    try:
        pe = Pelicula.objects.get(idPelicula = request.GET['txt_p_id'])
        pe.delete()
        msj = 'Pelicula eliminada'
        return render(request, "eliminar.html", {'msj': msj})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'Pelicula no existe'
        else:
            msj = 'Ha ocurrido un problema'   
        return render(request,"eliminar.html", {"msj":msj}) 

def fx_eliminarlibro(request):
    msj = None
    try:
        li = Libro.objects.get(idLibro = request.GET['txt_l_id'])
        li.delete()
        msj = 'Libro eliminado'
        return render(request, "eliminar.html", {'msj': msj})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'Libro no existe'
        else:
            msj = 'Ha ocurrido un problema'   
        return render(request,"inicio.html", {"msj":msj}) 

def fx_actualizar(request):
    msj = None
    try:
        cat = request.GET["select_categoria"]
        if cat == "J":
            cont = Juego.objects.get(idJuego = request.GET["txt_id_actualizar"])
            return render(request, "actualizar.html",{'contenido':cont,'vista':'J'})
        elif cat == "P":
            cont = Pelicula.objects.get(idPelicula = request.GET["txt_id_actualizar"])
            return render(request, "actualizar.html",{'contenido':cont,'vista':'P'})
        elif cat == "L":
            cont = Libro.objects.get(idLibro = request.GET["txt_id_actualizar"])
            return render(request, "actualizar.html",{'contenido':cont,'vista':'L'})
        else:
            msj = "Categoria no selecionada"
            return render(request, "actualizar.html",{'msj':msj})
    except:
        cont = None




