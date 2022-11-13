from django.shortcuts import render
from .clases.reservas import Reserva

listado = []

def inicio(request):
    return render(request, 'index.html')

def to_formularioReserva(request):
    return render(request, 'formReserva.html')

def to_listado(request):    
    return render(request, 'respListado.html',{"l":listado})

def to_formularioEliminar(request):
    return render(request, 'formEliminar.html')

def to_formularioBusqueda(request):
    return render(request, 'formBusqueda.html')
    
def to_formularioConfirmar(request):
    return render(request, 'formConfirmar.html')    

def fx_reservar(request):
    id = request.POST["txtId"]
    nombre = request.POST["txtNombre"]
    rut = request.POST["txtRut"]
    sexo = request.POST["txtSexo"]
    fechaNacimiento = request.POST["txtFechaNacimiento"]
    fechaReserva = request.POST["txtFechaReserva"]
    telefono = request.POST["txtTelfono"]
    habitacion = request.POST["txtHabitacion"]
    rev = Reserva(id,nombre,rut,sexo,fechaNacimiento,fechaReserva,telefono,habitacion)
    listado.append(rev)
    return render(request, 'respReserva.html',{"r":rev})

def fx_buscar(request):
    id = request.GET["txtId"]
    encontrado = ""
    for x in listado:
        if id == x.id:
            encontrado = x 
    return render(request, 'respBusqueda.html', {"r":encontrado})

def fx_eliminar(request):
    id = request.POST["txtId"]
    for x in listado:
        if id == x.id:
            listado.remove(x)
    return render(request, 'respListado.html',{"l":listado})

def fx_confirmarId(request):
    id = request.GET["txtId"]
    encontrado = ""
    for x in listado:
        if id == x.id:
            encontrado = x 
    return render(request, 'formActualizar.html', {"r":encontrado})

def fx_actualizar(request):
    id = request.POST["txtId"]
    nombre = request.POST["txtNombre"]
    rut = request.POST["txtRut"]
    sexo = request.POST["txtSexo"]
    fechaNacimiento = request.POST["txtFechaNacimiento"]
    fechaReserva = request.POST["txtFechaReserva"]
    telefono = request.POST["txtTelfono"]
    habitacion = request.POST["txtHabitacion"]
    rev = Reserva(id,nombre,rut,sexo,fechaNacimiento,fechaReserva,telefono,habitacion)
    for x in listado:
        if id == x.id:
            listado.remove(x)
    listado.append(rev)
    return render(request, 'respReserva.html',{"r":rev})        
    