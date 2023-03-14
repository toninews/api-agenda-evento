from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from agenda_evento.api.models import Evento


class EventoViews(GenericViewSet):

    def create(self, request):
        dados_response = {
            'mensagem': 'Dados recebidos com sucesso',
            'dados': request.data
        }
        return Response(dados_response, 200)

    def list(self, request):
        queryset = Evento.objects.all()

        for evento in queryset:
            print(evento)

        return Response(queryset, 200)
