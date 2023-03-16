from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from agenda_evento.api.models import Evento
from agenda_evento.api.serializers import EventoSerializer


class EventoViews(GenericViewSet):

    serializer_class = EventoSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        dados_response = {
            "evento_id": serializer.data['id'],
            'mensagem': f'Evento {serializer.data["titulo"]} criado com sucesso.'
        }
        return Response(dados_response, status.HTTP_201_CREATED)

    def list(self, request):
        queryset = Evento.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
