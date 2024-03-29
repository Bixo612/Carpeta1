from django.db import models


class Juego(models.Model):
    idJuego = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    an_o = models.IntegerField()
    clasificacion = models.CharField(max_length=10)
    consola = models.CharField(max_length=25)
    disponible = models.BooleanField(default=True)


class Pelicula(models.Model):
    idPelicula = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    an_o = models.IntegerField()
    clasificacion = models.CharField(max_length=10)
    director = models.CharField(max_length=50)
    duracion = models.IntegerField()
    disponible = models.BooleanField(default=True)


class Libro(models.Model):
    idLibro = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    an_o = models.IntegerField()
    escritor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    disponible = models.BooleanField(default=True)


class Disco(models.Model):
    idDisco = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    an_o = models.IntegerField()
    interprete = models.CharField(max_length=50)
    duracion = models.IntegerField()
    disponible = models.BooleanField(default=True)


class Vinilo(models.Model):
    idVinilo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    an_o = models.IntegerField()
    interprete = models.CharField(max_length=50)
    duracion = models.IntegerField()
    disponible = models.BooleanField(default=True)


class Genero(models.Model):
    idG = models.IntegerField(primary_key=True)
    genero = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)


class Usuario(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nick = models.CharField(max_length=50, unique=True)
    correo = models.CharField(max_length=100, unique=True)
    clave = models.CharField(max_length=100)
    fnacimiento = models.DateField()
    tipo = models.CharField(max_length=5)


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
(class) IntegerField(verbose_name: str | None = ..., name: str | None = ..., primary_key: bool = ..., max_length: int | None = ..., unique: bool = ..., blank: bool = ..., null: Literal[False] = ..., db_index: bool = ..., default: int | (() -> int) | None = ..., editable: bool = ..., auto_created: bool = ..., serialize: bool = ..., unique_for_date: str | None = ..., unique_for_month: str | None = ..., unique_for_year: str | None = ..., choices: Iterable[Tuple[int, str] | Tuple[str, Iterable[Tuple[int, str]]]] = ..., help_text: str = ..., db_column: str | None = ..., db_tablespace: str | None = ..., validators: Iterable[_ValidatorCallable] = ..., error_messages: _ErrorMessagesToOverride | None = ...)

IntegerField(verbose_name: str | None = ..., name: str | None = ..., primary_key: bool = ..., max_length: int | None = ..., unique: bool = ..., blank: bool = ..., null: Literal[True] = ..., db_index: bool = ..., default: int | (() -> int) = ..., editable: bool = ..., auto_created: bool = ..., serialize: bool = ..., unique_for_date: str | None = ..., unique_for_month: str | None = ..., unique_for_year: str | None = ..., choices: Iterable[Tuple[int, str] | Tuple[str, Iterable[Tuple[int, str]]]] = ..., help_text: str = ..., db_column: str | None = ..., db_tablespace: str | None = ..., validators: Iterable[_ValidatorCallable] = ..., error_messages: _ErrorMessagesToOverride | None = ...)
"""
