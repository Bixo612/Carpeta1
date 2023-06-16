alumnos = [{'nombre': 'Felipe', 'rut': '10789456-5', 'edad': '10', 'notas': {'Lenguaje': [], 'Ingles': []}},
           {'nombre': 'Sebastian', 'rut': '10159159-6','edad': '10', 'notas': {"Historia": [], "Musica":[]}},
           {'nombre': 'Matias', 'rut': '11256796-K', 'edad': '10', 'notas': {"Historia": [], "Quimica":[]}}]

ramos = ["Lenguaje", "Matemáticas", "Historia", "Ed. Fisica",
         "Quimica", "Biologia", "Musica", "Artistica", "Ingles"]


def fxIdReal(id):
    r = False
    if id.isnumeric():
        id = int(id)
        if id >= 0 and id <= len(alumnos):
            r = True
    return r


def fxRamoReal(id):
    r = False
    if id.isnumeric():
        id = int(id)
        if id >= 0 and id <= len(ramos):
            r = True
    return r


def fxCrearAlumno():
    print("===Crear Alumno===")
    nombre = input("Ingrese el nombre: ")
    rut = input("Ingrese el rut: ")
    edad = input("Ingrese la edad: ")
    notas = {}
    alumno = {
        "nombre": nombre,
        "rut": rut,
        "edad": edad,
        "notas": notas
    }
    alumnos.append(alumno)
    print("Alumno \n", alumno, "\n Registrado")


def fxEditarAlumno():
    id = input("Ingrese el id del alumno que desee editar: ")
    if fxIdReal(id):
        id = int(id)
        alumnoSelecionado = (alumnos[id])
        print(alumnoSelecionado)
        print("===Editar Alumno===")
        nombre = input("Ingrese el nombre: ")
        rut = input("Ingrese el rut: ")
        edad = input("Ingrese la edad: ")
        notas = alumnoSelecionado["notas"]
        alumnoActualizado = {
            "nombre": nombre,
            "rut": rut,
            "edad": edad,
            "notas": notas
        }
        alumnos[id] = alumnoActualizado
    else:
        print("Id de alumno no encontrado")


def fxEliminarAlumno():
    id = input("Ingrese el id del alumno que desee eliminar: ")
    if fxIdReal(id):
        eliminar = int(eliminar)
        alumnos.pop(eliminar)
    else:
        print("Id de alumno no encontrado")


def fxAgregarCarga():
    idAlumno = input("Ingrese el id del alumno que desee actualizar: ")
    if fxIdReal(idAlumno):
        idAlumno = int(idAlumno)
        alumnoSelecionado = alumnos[idAlumno]
        print(alumnoSelecionado)
        idRamo = input("Inngrese el id del ramo que desea agregar: ")
        if fxRamoReal(idRamo):
            idRamo = int(idRamo)
            ramoSelecionado = ramos[idRamo]
            notasAlumno = alumnoSelecionado["notas"]
            notasAlumno[ramoSelecionado] = []
            alumnoSelecionado["notas"] = notasAlumno
            alumnos[idAlumno] = alumnoSelecionado
        else:
            print("Id de ramo no encontrado")
    else:
        print("Id de alumno no encontrado")


def fxListarAlumnos():
    if len(alumnos) > 0:
        print("Id / Rut / Edad / Nombre")
        n = 0
        for i in alumnos:
            print("{} / {} / {} / {}".format(n,
                  i["rut"], i["edad"], i["nombre"]))
            n = n + 1

def fxListarAlumnosNotas():
    if len(alumnos) > 0:
        print("Id / Nombre / Notas")
        n = 0
        for i in alumnos:
            print("{} / {} / {}".format(n,
                  i["nombre"], i["notas"]))
            n = n + 1

def fxListarRamos():
    if len(ramos) > 0:
        n = 0
        for i in ramos:
            print("{} - {}".format(n, i))
            n = n + 1


def menu():
    salir = True
    menu = """===Menu de colegio=== 
    0   Salir
    1   Crear Alumno
    2   Editar Alumno
    3   Eliminar Alumno
    4   Listar Alumnos
    5   Agregar Carga académica
    6   Listar Ramos
    7   Listar Cargas por alumno"""

    while salir:
        print(menu)
        op = int(input("Eliga una opcion: "))
        if op == 0:
            salir = False
        elif op == 1:
            fxCrearAlumno()
        elif op == 2:
            fxEditarAlumno()
        elif op == 3:
            fxEliminarAlumno()
        elif op == 4:
            fxListarAlumnos()
        elif op == 5:
            fxAgregarCarga()
        elif op == 6:
            fxListarRamos()
        elif op == 7:
            fxListarAlumnosNotas()
        #
        elif op == 10:
            print(alumnos)  # Mostar lista de alumnos
        elif op == 11:
            print(len(alumnos))  # mostar cantidad de alumnos
        elif op == 12:
            for i in alumnos:  # Recorrer lista de alumnos
                print(i)


menu()
