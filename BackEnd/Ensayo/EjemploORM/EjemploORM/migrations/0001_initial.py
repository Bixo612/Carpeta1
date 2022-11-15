# Generated by Django 4.1.1 on 2022-10-27 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('rut', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('correo_electronico', models.CharField(max_length=40, unique=True)),
                ('direccion', models.CharField(max_length=50)),
                ('contrasenna', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
    ]