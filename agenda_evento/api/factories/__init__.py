import factory

from agenda_evento.api.models import Evento


class EventoFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Evento

    titulo = 'Call para Alinhar'
    data = '2022-05-10'
    horario_inicio = '13:00:00'
    horario_fim = '14:00:00'
    convidados = ['junior.tst@tst.com', 'junior.tst2@tst.com']
    local = 'Google Meet'
    descricao = 'Call de alinhamento dos novos módulos do curso'
