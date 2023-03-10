from django.test import Client


def test_deve_criar_evento(client: Client):
    dados_requisicao = {
        'titulo': 'Call de Alinhamento',
        'data': '30/04/2022',
        'horario_inicio': '16:40',
        'horario_fim': '17:08',
        'convidados': ['toninews57@gmail.com'],
        'local': 'https://meet.google.com/rbr-hhfr-mnt',
        'descricao': 'Call para alinhar módulo 19'
    }
    response = client.post(path='/api/v1/eventos/', data=dados_requisicao)

    assert response.status_code == 200

    mensagem_response = response.data['mensagem']
    assert mensagem_response == 'Dados recebidos com sucesso'

    dados_response = response.data['dados']
    assert dados_response['titulo'] == 'Call de Alinhamento'
    assert dados_response['data'] == '30/04/2022'
    assert dados_response['horario_inicio'] == '16:40'
    assert dados_response['horario_fim'] == '17:08'
    assert dados_response['convidados'] == 'toninews57@gmail.com'
    assert dados_response['local'] == 'https://meet.google.com/rbr-hhfr-mnt'
    assert dados_response['descricao'] == 'Call para alinhar módulo 19'


def test_deve_listar_evento(client: Client):
    response = client.get('/api/v1/eventos/')

    assert response.status_code == 200

    dados_response = response.data[0]
    assert dados_response['titulo'] == 'Call de Alinhamento'
    assert dados_response['data'] == '30/04/2022'
    assert dados_response['horario_inicio'] == '16:40'
    assert dados_response['horario_fim'] == '17:08'
    assert dados_response['convidados'] == ['toninews57@gmail.com']
    assert dados_response['local'] == 'https://meet.google.com/rbr-hhfr-mnt'
    assert dados_response['descricao'] == 'Call para alinhar módulo 19'
