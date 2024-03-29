# Generated by Django 4.1.1 on 2023-01-25 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('idDisco', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=10)),
                ('an_o', models.IntegerField()),
                ('interprete', models.CharField(max_length=50)),
                ('duracion', models.IntegerField()),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idG', models.IntegerField(primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('idJuego', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=10)),
                ('an_o', models.IntegerField()),
                ('clasificacion', models.CharField(max_length=10)),
                ('consola', models.CharField(max_length=25)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('idLibro', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=10)),
                ('an_o', models.IntegerField()),
                ('escritor', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=50)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('idPelicula', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=10)),
                ('an_o', models.IntegerField()),
                ('clasificacion', models.CharField(max_length=10)),
                ('director', models.CharField(max_length=50)),
                ('duracion', models.IntegerField()),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vinilo',
            fields=[
                ('idVinilo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=10)),
                ('an_o', models.IntegerField()),
                ('interprete', models.CharField(max_length=50)),
                ('duracion', models.IntegerField()),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
    ]
