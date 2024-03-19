from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Rutas para el Web Service
    path('api/eventos/', views.lista_eventos, name='lista_eventos_api'),
    path('api/eventos/<int:evento_id>/', views.detalle_evento, name='detalle_evento_api'),

    # Otras rutas para la aplicación web
    path('', views.inicio, name='inicio'),
    path('eventos/', views.lista_eventos_web, name='lista_eventos_web'),
    path('eventos/nuevo/', views.crear_evento, name='crear_evento'),
    path('eventos/<int:evento_id>/', views.detalle_evento_web, name='detalle_evento_web'),
    path('eventos/<int:evento_id>/editar/', views.editar_evento, name='editar_evento'),
    path('eventos/<int:evento_id>/eliminar/', views.eliminar_evento, name='eliminar_evento'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]
