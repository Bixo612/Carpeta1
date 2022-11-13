from dataclasses import dataclass
@dataclass

class Reserva:
    id:str
    nombre:str
    rut:str
    sexo:str
    fechaNacimiento:str
    fechaReserva:str
    telefono:str
    habitacion:str

    def getReserva(self):
        return self.id