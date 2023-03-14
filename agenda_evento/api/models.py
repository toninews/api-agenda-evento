from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.fields import CharField


class Evento(models.Model):
    titulo = CharField('TITULO', max_length=40, null=False)
    data = models.DateField('DATA', null=False)
    horario_inicio = models.TimeField('HORARIO_INICIO', null=False)
    horario_fim = models.TimeField('HORARIO_FIM', null=False)
    convidados = ArrayField(CharField('CONVIDADO', max_length=50), blank=False)
    local = models.CharField('LOCAL', max_length=200, null=False)
    descricao = models.CharField('DESCRICAO', max_length=200)
