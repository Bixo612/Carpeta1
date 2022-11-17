from django.db import models

class Juego(models.Model):
    idJuego         = models.CharField(max_length=10, primary_key=True)
    nombre          = models.CharField(max_length=100)
    consola         = models.CharField(max_length=25)
    genero          = models.CharField(max_length=10)
    an_o            = models.IntegerField()
    clasificacion   = models.CharField(max_length=10)

class Pelicula(models.Model):
    idPelicula      = models.CharField(max_length=10, primary_key=True)
    nombre          = models.CharField(max_length=100)
    director        = models.CharField(max_length=50)
    genero          = models.CharField(max_length=10)
    an_o            = models.IntegerField()
    clasificacion   = models.CharField(max_length=10)


"""
class Persona(models.Model):
    rut                 = models.CharField(primary_key=True, max_length=13)
    nombre              = models.CharField(max_length=20)
    correo_electronico  = models.CharField(unique=True, max_length=40)
    direccion           = models.CharField(max_length=50)
    contrasenna         = models.CharField(max_length=15)
    telefono            = models.CharField(max_length=15)
Juegos
    Id
    Nombre
    Consola
    Genero
    Año
    Clasificación
Peliculas
    Id
    Nombre
    Director
    Genero
    Año
    Clasificación
py manage.py makemigrations BlockBuster
python manage.py migrate
py manage.py runserver
"""