from django.db import models

class Persona(models.Model):
    rut                 = models.CharField(primary_key=True, max_length=13)
    nombre              = models.CharField(max_length=20)
    correo_electronico  = models.CharField(unique=True, max_length=40)
    direccion           = models.CharField(max_length=50)
    contrasenna         = models.CharField(max_length=15)
    telefono            = models.CharField(max_length=15)

