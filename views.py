from django.shortcuts import render
from django.http import JsonResponse
from .models import Evento
from django.contrib.auth import views as auth_views

# Vista para obtener la lista de eventos
def lista_eventos(request):
    eventos = Evento.objects.all()
    data = [{'id': evento.id, 'titulo': evento.titulo, 'descripcion': evento.descripcion,
             'fecha_inicio': evento.fecha_inicio, 'fecha_fin': evento.fecha_fin} for evento in eventos]
    return JsonResponse(data, safe=False)

# Vista para obtener detalles de un evento específico
def detalle_evento(request, evento_id):
    try:
        evento = Evento.objects.get(pk=evento_id)
        data = {'id': evento.id, 'titulo': evento.titulo, 'descripcion': evento.descripcion,
                'fecha_inicio': evento.fecha_inicio, 'fecha_fin': evento.fecha_fin}
        return JsonResponse(data)
    except Evento.DoesNotExist:
        return JsonResponse({'error': 'Evento no encontrado'}, status=404)

# Otras vistas para crear, editar y eliminar eventos...

# Vista para el inicio de sesión
class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'