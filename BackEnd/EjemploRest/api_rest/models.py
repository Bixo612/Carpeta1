from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel, SoftDeletableModel

class Mensaje(TimeStampedModel, SoftDeletableModel):
    id_mensaje = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=50, null=False, blank=True)
    mensaje = models.TextField(max_length=5000, null=False, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="fecha actualización")
    
    def __str__(self):
        return self.titulo