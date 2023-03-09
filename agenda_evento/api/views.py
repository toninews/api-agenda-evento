from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response


class EventoViews(GenericViewSet):

    def create(self, request):
        return Response('Evento recebido', 200)
