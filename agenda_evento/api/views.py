from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from agenda_evento.api.models import Evento
from agenda_evento.api.serializers import EventoSerializer


class EventoViews(GenericViewSet):

    serializer_class = EventoSerializer
    queryset = Evento.objects.all()

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
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk):
        evento = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(evento)
        return Response(serializer.data)

    def update(self, request, pk):
        evento = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(evento, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        evento = get_object_or_404(self.queryset, pk=pk)
        evento.delete()
        return Response(
            {
                'id':pk, 'mensagem': 'Evento removido com sucesso.'
            }
        )
