from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter

from agenda_evento.api.views import EventoViews


rota_eventos = DefaultRouter()
rota_eventos.register('eventos', EventoViews, basename='EventoViews')

app_name = 'api'

urlpatterns = (
    path('', include(rota_eventos.urls)),

)
