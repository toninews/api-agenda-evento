from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from agenda_evento.api.models import Evento


class EventoSerializer(ModelSerializer):
    convidados = serializers.ListField(
        child=serializers.CharField(max_length=50),
        allow_empty=False
    )

    class Meta:
        model = Evento
        fields = '__all__'

    def to_internal_value(self, data):
        mutable_data = data.copy()
        convidados = mutable_data.get('convidados')

        if isinstance(convidados, str):
            mutable_data['convidados'] = [
                item.strip() for item in convidados.split(',') if item.strip()
            ]

        return super().to_internal_value(mutable_data)
