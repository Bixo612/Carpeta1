from django.shortcuts import render, redirect
from msilib.schema import Error
from .models import Juego, Pelicula, Libro, Disco, Vinilo, Genero, Usuario


def irInicio(request):
    return render(request, "inicio.html")


def irRegistro(request):
    gen = Genero.objects.all()
    return render(request, "registro.html", {'generos': gen, 'alert': False})


def irCategorias(request):
    gen = Genero.objects.all()
    return render(request, "categorias.html", {'generos': gen, 'alert': False})


def irBuscar_Eliminar(request):
    return render(request, "buscar_eliminar.html")


def irCrearUsuario(request):
    return render(request, "usuarios/crearUsuario.html", {'alert': False})


def irBuscarUsuario(request):
    usr = Usuario.objects.all()
    return render(request, "usuarios/buscarUsuario.html", {'usr': usr})


def irLista(request):
    p = Pelicula.objects.all()
    j = Juego.objects.all()
    l = Libro.objects.all()
    d = Disco.objects.all()
    v = Vinilo.objects.all()
    return render(request, "lista.html", {'juegos': j, 'peliculas': p, 'libros': l, 'discos': d, 'vinilos': v})


def irEditar(request):
    gen = Genero.objects.all()
    id = request.GET['txt_id']
    id = id.upper()
    if id[0] == 'J':
        try:
            cont = Juego.objects.get(idJuego=id)
            return render(request, "editar.html", {'vista': 'J', 'cont': cont, 'generos': gen})
        except:
            pass
    elif id[0] == 'P':
        try:
            cont = Pelicula.objects.get(idPelicula=id)
            return render(request, "editar.html", {'vista': 'P', 'cont': cont, 'generos': gen})
        except:
            pass
    elif id[0] == 'L':
        try:
            cont = Libro.objects.get(idLibro=id)
            return render(request, "editar.html", {'vista': 'L', 'cont': cont, 'generos': gen})
        except:
            pass
    elif id[0] == 'D':
        try:
            cont = Disco.objects.get(idDisco=id)
            return render(request, "editar.html", {'vista': 'D', 'cont': cont, 'generos': gen})
        except:
            pass
    elif id[0] == 'V':
        try:
            cont = Vinilo.objects.get(idVinilo=id)
            return render(request, "editar.html", {'vista': 'V', 'cont': cont, 'generos': gen})
        except:
            pass
    else:
        pass

def alertEliminar(request):
    id = request.GET['txt_id']
    id = id.upper()
    if id[0] == 'J':
        try:
            cont = Juego.objects.get(idJuego=id)
            return render(request, "buscar.html", {'vista': 'J', 'cont': cont,'alert': True})
        except:
            return render(request, "inicio.html")
    else:
        return render(request, "inicio.html")

def irEliminarUsuario(request):
    rutDel = request.GET['inptName']
    usr = Usuario.objects.get(rut=rutDel)
    return render(request, 'usuarios/eliminarUsuario.html', {'usr': usr})


def irEditarUsuario(request):
    rutEdt = request.GET['inptName']
    usr = Usuario.objects.get(rut=rutEdt)
    return render(request, 'usuarios/editarUsuario.html', {'usr': usr})


def fx_editarUsuario(request):
    msj = None
    u_rut = request.GET['inpt_rut']
    u_nick = request.GET['inpt_nick']
    u_correo = request.GET['inpt_correo']
    u_naciemiento = request.GET['inpt_nacimiento']
    u_tipo = request.GET['inpt_tipo']
    try:
        ur = Usuario.objects.get(rut=u_rut)
        ur.nick = u_nick
        ur.correo = u_correo
        ur.fnacimiento = u_naciemiento
        ur.tipo = u_tipo
        try:
            ur.save()
            msj = "Se ha actualizado el usuario"
            usr = Usuario.objects.all()
            return render(request, "usuarios/buscarUsuario.html", {'msj': msj, 'usr': usr, "alert": True, 'busqueda': True, "find": ur})
        except:
            msj = "Ha ocurrido un error :c"
    except:
        msj = "Ha ocurrido un error :c"
    return render(request, "inicio.html", {'msj': msj})


def fx_editarJuego(request):
    msj = None
    j_id = request.POST['txt_j_id']
    j_nombre = request.POST['txt_j_nombre']
    j_consola = request.POST['txt_j_consola']
    j_genero = request.POST['txt_j_genero']
    j_ano = request.POST['txt_j_ano']
    j_clasificacion = request.POST['txt_j_clasificacion']
    j_disponible = request.POST['txt_j_disponible']
    try:
        edi = Juego.objects.get(idJuego=j_id)
        edi.nombre = j_nombre
        edi.consola = j_consola
        edi.genero = j_genero
        edi.an_o = j_ano
        edi.clasificacion = j_clasificacion
        edi.disponible = j_disponible
        try:
            edi.save()
            msj = "Se ha actualizado el juego"
        except:
            pass
    except:
        pass
    return render(request, "inicio.html", {'msj': msj})


def fx_editarDisco(request):
    msj = None
    d_id = request.POST['txt_d_id']
    d_nombre = request.POST['txt_d_nombre']
    d_genero = request.POST['txt_d_genero']
    d_ano = request.POST['txt_d_ano']
    d_interprete = request.POST['txt_d_interprete']
    d_duracion = request.POST['txt_d_duracion']
    d_disponible = request.POST['txt_d_disponible']
    try:
        dis = Disco.objects.get(idDisco=d_id)
        dis.nombre = d_nombre
        dis.genero = d_genero
        dis.an_o = d_ano
        dis.interprete = d_interprete
        dis.duracion = d_duracion
        dis.disponible = d_disponible
        try:
            dis.save()
            msj = "Se ha actualizado el disco"
        except:
            pass
    except:
        pass
    return render(request, "inicio.html", {'msj': msj})


def fx_editarVinilo(request):
    msj = None
    v_id = request.POST['txt_v_id']
    v_nombre = request.POST['txt_v_nombre']
    v_genero = request.POST['txt_v_genero']
    v_ano = request.POST['txt_v_ano']
    v_interprete = request.POST['txt_v_interprete']
    v_duracion = request.POST['txt_v_duracion']
    v_disponible = request.POST['txt_v_disponible']
    try:
        dis = Vinilo.objects.get(idDisco=v_id)
        dis.nombre = v_nombre
        dis.genero = v_genero
        dis.an_o = v_ano
        dis.interprete = v_interprete
        dis.duracion = v_duracion
        dis.disponible = v_disponible
        try:
            dis.save()
            msj = "Se ha actualizado el vinilo"
        except:
            pass
    except:
        pass
    return render(request, "inicio.html", {'msj': msj})


def fx_editarLibro(request):
    msj = None
    l_id = request.POST['txt_l_id']
    l_nombre = request.POST['txt_l_nombre']
    l_genero = request.POST['txt_l_genero']
    l_ano = request.POST['txt_l_ano']
    l_escritor = request.POST['txt_l_escritor']
    l_editorial = request.POST['txt_l_editorial']
    l_disponible = request.POST['txt_l_disponible']
    try:
        lib = Libro.objects.get(idLibro=l_id)
        lib.nombre = l_nombre
        lib.genero = l_genero
        lib.an_o = l_ano
        lib.escritor = l_escritor
        lib.editorial = l_editorial
        lib.disponible = l_disponible
        try:
            lib.save()
            msj = "Se ha actualizado el libro"
        except:
            msj = "error"
    except:
        msj = "error"
    return render(request, "inicio.html", {'msj': msj})


def fx_editarPelicula(request):
    msj = None
    p_id = request.POST['txt_p_id']
    p_nombre = request.POST['txt_p_nombre']
    p_genero = request.POST['txt_p_genero']
    p_ano = request.POST['txt_p_ano']
    p_clasificacion = request.POST['txt_p_clasificacion']
    p_disponible = request.POST['txt_p_disponible']
    p_director = request.POST['txt_p_director']
    p_duracion = request.POST['txt_p_duracion']
    try:
        edita = Pelicula.objects.get(idPelicula=p_id)
        edita.nombre = p_nombre
        edita.genero = p_genero
        edita.an_o = p_ano
        edita.clasificacion = p_clasificacion
        edita.director = p_disponible
        edita.disponible = p_director
        edita.duracion = p_duracion
        try:
            edita.save()
            msj = "Se ha actualizado la pelicula"
        except:
            pass
    except:
        pass
    return render(request, "inicio.html", {'msj': msj})


def fx_buscar(request):
    id = request.POST['txt_id']
    id = id.upper()
    if id[0] == 'L':
        try:
            cont = Libro.objects.get(idLibro=id)
            return render(request, 'buscar.html', {'vista': 'L', 'cont': cont})
        except:
            pass
    elif id[0] == 'P':
        try:
            cont = Pelicula.objects.get(idPelicula=id)
            return render(request, 'buscar.html', {'vista': 'P', 'cont': cont})
        except:
            pass
    elif id[0] == 'J':
        try:
            cont = Juego.objects.get(idJuego=id)
            return render(request, 'buscar.html', {'vista': 'J', 'cont': cont})
        except:
            pass
    elif id[0] == 'D':
        try:
            cont = Disco.objects.get(idDisco=id)
            return render(request, 'buscar.html', {'vista': 'D', 'cont': cont})
        except:
            pass
    elif id[0] == 'V':
        try:
            cont = Vinilo.objects.get(idVinilo=id)
            return render(request, 'buscar.html', {'vista': 'V', 'cont': cont})
        except:
            pass
    else:
        # en caso de no coincidir con el formato mantien en la misma pagina
        try:
            return redirect(request.META['HTTP_REFERER'])
        except:
            return render(request, "inicio.html")


def fx_buscarUsuario(request):
    msj = "Usuario no encontrado"
    usr = Usuario.objects.all()
    parametro = request.POST["inptParametro"]
    dato = request.POST["inptDato"]
    if parametro == "R":
        try:
            find = Usuario.objects.get(rut=dato)
            return render(request, "usuarios/buscarUsuario.html", {'usr': usr, 'busqueda': True, "find": find})
        except:
            return render(request, "usuarios/buscarUsuario.html", {'usr': usr, "alert": True, "busqueda": False, "msj": msj})
    elif parametro == "N":
        try:
            find = Usuario.objects.get(nick=dato)
            return render(request, "usuarios/buscarUsuario.html", {'usr': usr, 'busqueda': True, "find": find})
        except:
            return render(request, "usuarios/buscarUsuario.html", {'usr': usr, "alert": True, "busqueda": False, "msj": msj})
    elif parametro == "C":
        try:
            find = Usuario.objects.get(correo=dato)
            return render(request, "usuarios/buscarUsuario.html", {'usr': usr, 'busqueda': True, "find": find})
        except:
            return render(request, "usuarios/buscarUsuario.html", {'usr': usr, "alert": True, "busqueda": False, "msj": msj})
    else:
        return render(request, "inicio.html")


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
    return render(request, "registro.html", {'msj': msj, 'alert': True})


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
    return render(request, "registro.html", {'msj': msj, 'alert': True})


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
    return render(request, "registro.html", {'msj': msj, 'alert': True})


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
    return render(request, "registro.html", {'msj': msj, 'alert': True})


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
    return render(request, "registro.html", {'msj': msj, 'alert': True})


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
    return render(request, "categorias.html", {'generos': gen, 'msj': msj, 'alert': True})


def fx_registrarUsuario(request):
    msj = None
    inptClave1 = request.POST['inpt_clave1']
    inptClave2 = request.POST['inpt_clave2']
    if inptClave1 != inptClave2:
        msj = "Las claves no coinciden"
        return render(request, "usuarios/crearUsuario.html", {'alert': True, 'msj': msj})
    else:
        inptRut = request.POST['inpt_rut']
        inptNick = request.POST['inpt_nick']
        inptCorreo = request.POST['inpt_correo']
        inptNacimiento = request.POST['inpt_nacimiento']
        inptTipo = request.POST['inpt_tipo']
        try:
            Usuario.objects.create(rut=inptRut,
                                   nick=inptNick,
                                   correo=inptCorreo,
                                   clave=inptClave2,
                                   fnacimiento=inptNacimiento,
                                   tipo=inptTipo
                                   )
            msj = f"\nUsuario {inptNick} registrado correctamente :)"
        except Error as err:
            msj = f'\n Ha ocurrido un error en la operacion {err}'
        return render(request, "usuarios/crearUsuario.html", {'alert': True, 'msj': msj})


def fx_eliminarGenero(request):
    msj = None
    gen = Genero.objects.all()
    try:
        ge = Genero.objects.get(idG=request.GET['f_g_id'])
        ge.delete()
        msj = 'Genero eliminado correctamente'
        return render(request, "categorias.html", {'generos': gen, "msj": msj, 'alert': True})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'Genero no existe'
        else:
            msj = 'Ha ocurrido un problema'
        return render(request, "categorias.html", {'generos': gen, "msj": msj, 'alert': True})


def fx_eliminarUsuario(request):
    usr = Usuario.objects.all()
    msj = None
    try:
        usrDel = Usuario.objects.get(rut=request.GET['inptRut'])
        usrDel.delete()
        msj = "Usuario eliminado"
        return render(request, "usuarios/buscarUsuario.html", {"usr": usr, "msj": msj, 'alert': True})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'Usuario no existe'
        else:
            msj = 'Ha ocurrido un problema'
        return render(request, "usuarios/buscarUsuario.html", {"usr": usr, "msj": msj, 'alert': True})


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
