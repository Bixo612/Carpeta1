from django.db import models

class Persona(models.Model):
    rut = models.CharField(max_length = 13, primary_key = True)
    nombre = models.CharField(max_length = 20)
    correo_electronico = models.CharField(max_length = 40, unique = True)
    direccion = models.CharField(max_length = 50) 
    contrasenna = models.CharField(max_length = 15) 
    telefono = models.CharField(max_length = 15)
