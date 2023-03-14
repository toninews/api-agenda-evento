# Generated by Django 4.1.7 on 2023-03-13 19:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40, verbose_name='TITULO')),
                ('data', models.DateField(verbose_name='DATA')),
                ('horario_inicio', models.TimeField(verbose_name='HORARIO_INICIO')),
                ('horario_fim', models.TimeField(verbose_name='HORARIO_FIM')),
                ('convidados', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50, verbose_name='CONVIDADO'), size=None)),
                ('local', models.CharField(max_length=200, verbose_name='LOCAL')),
                ('descricao', models.CharField(max_length=200, verbose_name='DESCRICAO')),
            ],
        ),
    ]
