from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response


class EventoViews(GenericViewSet):

    def create(self, request):
        dados_response = {
            'mensagem': 'Dados recebidos com sucesso',
            'dados': request.data
        }
        return Response(dados_response, 200)

    def list(self, request):
        response_listagem_evento = [
            {
                "titulo": "Call de Alinhamento",
                "data": "30/04/2022",
                "horario_inicio": "16:40",
                "horario_fim": "17:08",
                "convidados": ["toninews57@gmail.com"],
                "local": "https://meet.google.com/rbr-hhfr-mnt",
                "descricao": "Call para alinhar módulo 19"
            }
        ]
        return Response(response_listagem_evento, 200)
