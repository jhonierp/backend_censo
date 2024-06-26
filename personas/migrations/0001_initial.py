# Generated by Django 4.2.2 on 2024-05-14 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('familias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=150)),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cedula'), ('RC', 'Registro Civil'), ('NUIP', 'Numero único de Identificación Personal'), ('TI', 'Tarjeta de Identidad')], max_length=4, null=True)),
                ('numero_documento', models.IntegerField()),
                ('exp_documento', models.DateField()),
                ('fecha_nacimiento', models.DateField()),
                ('parentesco', models.CharField(choices=[('PA', 'Padre'), ('MA', 'Madre'), ('CO', 'Conyugue'), ('HE', 'Hermano(a)'), ('CF', 'Cabeza De Familia'), ('ES', 'Esposa'), ('HI', 'Hijo (a)'), ('YR', 'Yerno'), ('NU', 'Nuera'), ('SU', 'Suegro (a)'), ('SO', 'Sobrino (a)'), ('CU', 'Cuñado (a)'), ('TI', 'Tio (a)'), ('AB', 'Abuelo (a)')], max_length=2, null=True)),
                ('sexo', models.CharField(max_length=100)),
                ('estado_civil', models.CharField(max_length=100)),
                ('profesion', models.CharField(max_length=150)),
                ('escolaridad', models.CharField(choices=[('SC', 'Secundaria'), ('PR', 'Primaria'), ('UN', 'Universitaria'), ('NI', 'Ninguno')], max_length=2, null=True)),
                ('integrantes', models.IntegerField()),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=150)),
                ('usuario', models.CharField(max_length=150)),
                ('familida_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='familias.familia')),
            ],
        ),
    ]
