import pytest

from agenda_evento.api.factories import EventoFactory


@pytest.fixture
def evento_factory():
    return EventoFactory()