from django import forms

from agenda_evento.api.models import Evento


class EventoForm(forms.ModelForm):
    convidados = forms.CharField(
        help_text='Separe os nomes por virgula. Exemplo: Ana, Bruno, Carlos',
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ana, Bruno, Carlos'})
    )

    class Meta:
        model = Evento
        fields = [
            'titulo',
            'data',
            'horario_inicio',
            'horario_fim',
            'convidados',
            'local',
            'descricao',
        ]
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'horario_fim': forms.TimeInput(attrs={'type': 'time'}),
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.initial['convidados'] = ', '.join(self.instance.convidados)

    def clean_convidados(self):
        convidados = self.cleaned_data['convidados']
        lista_convidados = [
            item.strip() for item in convidados.split(',') if item.strip()
        ]

        if not lista_convidados:
            raise forms.ValidationError('Informe ao menos um convidado.')

        return lista_convidados
