from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from agenda_evento.api.models import Evento
from agenda_evento.api.serializers import EventoSerializer


class EventoViews(GenericViewSet):

    serializer_class = EventoSerializer

    def create(self, request):
        dados_response = {
            'mensagem': 'Dados recebidos com sucesso',
            'dados': request.data
        }
        return Response(dados_response, 200)

    def list(self, request):
        queryset = Evento.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, 200)
