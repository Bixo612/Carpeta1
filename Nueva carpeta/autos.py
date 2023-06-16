clientes = []
autos = [
    {'patente': 'HTYU89', 'marca': 'Nissan', 'modelo': 'V 16', 'año': '1999'},
    {'patente': 'TY8963', 'marca': 'Suzuki', 'modelo': 'Alto', 'año': '2002'}
]


def crearVehiculo():
    print("Ingrese los datos del vehiculo:")
    patente = input("Patente: ")
    patente = patente.upper()
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = input("Año: ")
    vehiculo = {
        "patente": patente,
        "marca": marca,
        "modelo": modelo,
        "año": año,
    }
    autos.append(vehiculo)


def listarVehiculos():
    if len(autos) == 0:
        print("No hay vehiculos registrados")
    else:
        for i in autos:
            print(
                "{} - {} - {} - {} ".format(i["patente"], i["año"], i["modelo"], i["marca"]))


def txtMenu():
    menu = """===Menu de autos===
    0   Salir
    1   Agregar Vehiculo
    2   Listar Vehiculos"""
    print(menu)


def menu():
    salir = True
    while salir:
        txtMenu()
        op = int(input("Eliga una opcion: "))
        if op == 0:
            print("Adios :)")
            salir = False
        elif op == 1:
            crearVehiculo()
        elif op == 2:
            listarVehiculos()
        ################################
        elif op == -1:
            for i in autos:
                print(i)
        elif op == -2:
            print(autos)
        else:
            print("La opcion", op, "no es una opcion valida")


menu()
