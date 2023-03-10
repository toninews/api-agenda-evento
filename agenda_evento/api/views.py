from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response


class EventoViews(GenericViewSet):

    def create(self, request):
        dados_response = {
            'mensagem': 'Dados recebidos com sucesso',
            'dados': request.data
        }
        return Response(dados_response, 200)
