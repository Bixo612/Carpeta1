# Generated by Django 4.1.4 on 2022-12-07 10:13

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id_mensaje', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(blank=True, max_length=50)),
                ('mensaje', models.TextField(blank=True, max_length=5000)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='fecha actualización')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
