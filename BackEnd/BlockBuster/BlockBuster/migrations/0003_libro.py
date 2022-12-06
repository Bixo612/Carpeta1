# Generated by Django 4.1.1 on 2022-12-06 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlockBuster', '0002_remove_juego_id_remove_pelicula_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('idLibro', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('escritor', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=10)),
                ('an_o', models.IntegerField()),
                ('clasificacion', models.CharField(max_length=10)),
            ],
        ),
    ]