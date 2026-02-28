from django.shortcuts import get_object_or_404, redirect, render

from agenda_evento.api.models import Evento
from agenda_evento.base.forms import EventoForm


def home(request):
    success = request.GET.get('success') == '1'
    deleted = request.GET.get('deleted') == '1'
    edited = request.GET.get('edited') == '1'
    edit_id = request.GET.get('edit')
    evento_edicao = get_object_or_404(Evento, pk=edit_id) if edit_id else None

    if request.method == 'POST':
        if request.POST.get('action') == 'delete':
            evento = get_object_or_404(Evento, pk=request.POST.get('evento_id'))
            evento.delete()
            return redirect('/?deleted=1#painel-eventos')

        evento_id = request.POST.get('evento_id')
        instancia = get_object_or_404(Evento, pk=evento_id) if evento_id else None
        form = EventoForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            if instancia:
                return redirect('/?edited=1#painel-eventos')
            return redirect('/?success=1#painel-eventos')
    else:
        form = EventoForm(instance=evento_edicao)

    eventos = Evento.objects.order_by('-data', '-horario_inicio')[:6]

    return render(
        request,
        'base/home.html',
        {
            'form': form,
            'eventos': eventos,
            'success': success,
            'deleted': deleted,
            'edited': edited,
            'evento_edicao': evento_edicao,
        }
    )
