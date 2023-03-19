import pytest

from agenda_evento.api.factories import EventoFactory


@pytest.fixture
def evento_factory():
    return EventoFactory()


@pytest.fixture
def corpo_requisicao():
    return {
        'titulo': 'Call de Alinhamento',
        'data': '2021-12-09',
        'horario_inicio': '13:00',
        'horario_fim': '14:00',
        'convidados': ['toninews57@gmail.com'],
        'local': 'https://meet.google.com/rbr-hhfr-mnt',
        'descricao': 'Call para alinhar próximos módulos do curso'
    }
