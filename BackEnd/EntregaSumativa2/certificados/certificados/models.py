from django.db import models

class Certificado(models.Model):
    id_certificado = models.CharField(max_length=30, primary_key= True)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    curso = models.CharField(max_length=30)
    version = models.CharField(max_length=15) 
    id_verificacion = models.CharField(max_length=15)

'''
create database sistema_certificados;
use sistema_certificados;
create table certificados_certificado
(
    Id_certificado varchar(30) primary key,
    nombre varchar(50) not null,
    fecha date not null,
    curso varchar(30) not null,
    versión varchar(15) not null,
    id_verificacion varchar(15) not null unique
);
'''