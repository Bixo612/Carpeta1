# Generated by Django 4.1.1 on 2023-02-02 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlockBuster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nick', models.CharField(max_length=50, unique=True)),
                ('correo', models.CharField(max_length=100, unique=True)),
                ('clave', models.CharField(max_length=100)),
                ('fnacimiento', models.DateField()),
                ('tipo', models.CharField(max_length=5)),
            ],
        ),
    ]