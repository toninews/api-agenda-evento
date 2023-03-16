import pytest
import datetime

from agenda_evento.api.serializers import EventoSerializer


pytestmark = pytest.mark.django_db


def test_deve_serializar_evento(evento_factory):
    serializer = EventoSerializer(evento_factory)

    assert isinstance(serializer.data, dict)

    assert serializer.data['titulo'] == 'Call para Alinhar'
    assert serializer.data['data'] == '2022-05-10'
    assert serializer.data['horario_inicio'] == '13:00:00'
    assert serializer.data['horario_fim'] == '14:00:00'
    assert serializer.data['convidados'] == ['junior.tst@tst.com', 'junior.tst2@tst.com']
    assert serializer.data['local'] == 'Google Meet'
    assert serializer.data['descricao'] == 'Call de alinhamento dos novos módulos do curso'


def test_deve_desserializar_evento():
    evento = {
        'titulo': 'Call para Alinhar 99',
        'data': '2022-05-10',
        'horario_inicio': '13:00:00',
        'horario_fim': '14:00:00',
        'convidados': ['junior.tst@tst.com', 'junior.tst2@tst.com'],
        'local': 'Google Meet',
        'descricao': 'Call de alinhamento dos novos módulos do curso'
    }

    serializer = EventoSerializer(data=evento)

    assert serializer.is_valid()

    evento_desserializado = serializer.save()

    assert isinstance(evento_desserializado, object)

    assert evento_desserializado.titulo == 'Call para Alinhar 99'
    assert evento_desserializado.data == datetime.date(2022, 5, 10)
    assert evento_desserializado.horario_inicio == datetime.time(13, 0)
    assert evento_desserializado.horario_fim == datetime.time(14, 0)
    assert evento_desserializado.convidados == ['junior.tst@tst.com', 'junior.tst2@tst.com']
    assert evento_desserializado.local == 'Google Meet'
    assert evento_desserializado.descricao == 'Call de alinhamento dos novos módulos do curso'
