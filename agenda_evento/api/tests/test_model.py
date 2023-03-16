import pytest

from agenda_evento.api.models import Evento


@pytest.mark.django_db
def test_deve_criar_evento_na_base(evento_factory):
    assert evento_factory.titulo == 'Call para Alinhar'
    assert evento_factory.data == '2022-05-10'
    assert evento_factory.horario_inicio == '13:00:00'
    assert evento_factory.horario_fim == '14:00:00'
    assert evento_factory.convidados == ['junior.tst@tst.com', 'junior.tst2@tst.com']
    assert evento_factory.local == 'Google Meet'
    assert evento_factory.descricao == 'Call de alinhamento dos novos módulos do curso'

    assert Evento.objects.count() == 1