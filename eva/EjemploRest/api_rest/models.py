from django.db import models

# Create your models here.

from model_utils.models import TimeStampedModel, SoftDeletableModel

class Mensaje(TimeStampedModel, SoftDeletableModel):
    id_mensaje = models.IntegerField(primary_key= True)
    titulo = models.CharField(max_length=50, null= False, blank= True)
    mensaje = models.CharField(max_length=5000, null= False, blank= True)
    fecha_publicacion = models.DateTimeField(auto_now_add= True, verbose_name = 'Fecha Creacion')
    fecha_actualizacion = models.DateField(auto_now= True, verbose_name = 'Fecha Actualizacion')