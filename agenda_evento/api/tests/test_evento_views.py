import pytest

from django.test import Client
from rest_framework import status


PATH = '/api/v1/eventos/'
pytestmark = pytest.mark.django_db


def test_deve_criar_evento(client: Client, corpo_requisicao):
    response = client.post(path=PATH, data=corpo_requisicao)

    assert response.status_code == status.HTTP_201_CREATED

    mensagem_response = response.data['mensagem']
    assert mensagem_response == f'Evento {corpo_requisicao["titulo"]} criado com sucesso.'


def test_deve_listar_evento(client: Client, evento_factory):
    response = client.get(PATH)

    assert response.status_code == 200

    dados_response = response.data[0]
    assert dados_response['titulo'] == 'Call para Alinhar'
    assert dados_response['data'] == '2022-05-10'
    assert dados_response['horario_inicio'] == '13:00:00'
    assert dados_response['horario_fim'] == '14:00:00'
    assert dados_response['convidados'] == ['junior.tst@tst.com', 'junior.tst2@tst.com']
    assert dados_response['local'] == 'Google Meet'
    assert dados_response['descricao'] == 'Call de alinhamento dos novos módulos do curso'


def test_nao_deve_criar_evento_com_body_vazio(client: Client):
    request = {}

    response = client.post(PATH, data=request)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['titulo'] == ['This field is required.']
    assert response.data['data'] == ['This field is required.']
    assert response.data['horario_inicio'] == ['This field is required.']
    assert response.data['horario_fim'] == ['This field is required.']
    assert response.data['convidados'] == ['This field is required.']
    assert response.data['local'] == ['This field is required.']
    assert response.data['descricao'] == ['This field is required.']


def test_nao_deve_criar_evento_com_data_invalida(client: Client, corpo_requisicao):
    corpo_requisicao['data'] = '12/10/2022'
    response = client.post(PATH, data=corpo_requisicao)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['data'] == ['Date has wrong format. Use one of these formats instead: YYYY-MM-DD.']


def test_nao_deve_criar_evento_com_horas_invalidas(client: Client, corpo_requisicao):
    corpo_requisicao['horario_inicio'] = '1h'
    corpo_requisicao['horario_fim'] = '5 horas'
    response = client.post(PATH, data=corpo_requisicao)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['horario_inicio'] == ['Time has wrong format. Use one of these formats instead: '
                                               'hh:mm[:ss[.uuuuuu]].']
    assert response.data['horario_fim'] == ['Time has wrong format. Use one of these formats instead: '
                                            'hh:mm[:ss[.uuuuuu]].']


def test_deve_listar_evento_por_id(client: Client, corpo_requisicao):
    corpo_requisicao['titulo'] = 'Teste Evento por Id'

    response_post = client.post(PATH, data=corpo_requisicao)
    evento_id = response_post.data['evento_id']

    response = client.get(f'{PATH}{evento_id}/')

    assert response.status_code == status.HTTP_200_OK

    assert response.data['id'] == evento_id
    assert response.data['titulo'] == 'Teste Evento por Id'
    assert response.data['data'] == '2021-12-09'
    assert response.data['horario_inicio'] == '13:00:00'
    assert response.data['horario_fim'] == '14:00:00'
    assert response.data['convidados'] == ['toninews57@gmail.com']
    assert response.data['local'] == 'https://meet.google.com/rbr-hhfr-mnt'
    assert response.data['descricao'] == 'Call para alinhar próximos módulos do curso'


def test_nao_deve_listar_evento_nao_econtrado(client: Client):
    response = client.get(f'{PATH}1000/')

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == {'detail': 'Not found.'}
