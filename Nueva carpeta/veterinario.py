class Veterinario:
    def __init__(self, nombre, apellido, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad

class Due_o:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mascotas = []


class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

opciones = ["Opción 1", "Opción 2", "Opción 3", "Salir"]


def mostrar_menu():
    print("MENU:")
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")
    seleccion = input("Seleccione una opción: ")
    return seleccion


seleccion = ""
while seleccion != "0":
    seleccion = mostrar_menu()
    if seleccion == "1":
        print("Ha seleccionado la opción 1.")
    elif seleccion == "2":
        print("Ha seleccionado la opción 2.")
    elif seleccion == "3":
        print("Ha seleccionado la opción 3.")
    elif seleccion == "0":
        print("¡Hasta luego!")
    else:
        print("Selección inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    mostrar_menu()
