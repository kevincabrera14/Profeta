from django.urls import path
from django.contrib.auth import views as auth_views  # Agrega esta línea

from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('iniciar/', views.iniciar, name='iniciar'),
    path('pprincipal/', views.iniciar, name='pprincipal'),
    path('cerrar_session/', views.cerrar_session, name='cerrar_session'),
    path('perfil/', views.perfil, name='perfil'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('guardar/', views.guardar, name='guardar'),
    path('guardar_cambios/<str:correo>/', views.guardar_cambios_usuario, name='guardar_cambios'),
    path('agregar_mensaje/', views.agregar_mensaje, name='agregar_mensaje'),
    path('formulario-mensaje/', views.formulario_mensaje, name='formulario_mensaje'),
    path('inicio-profesor/', views.inicio_profesor, name='inicio_profesor'),
    path('mensajes-profesor/', views.mensajes_profesor, name='mensajes_profesor'),
    path('eliminar-mensaje/<int:mensaje_id>/', views.eliminar_mensaje, name='eliminar_mensaje'),
    path('eliminar_mensaje/<int:mensaje_id>/', views.eliminar_mensaje, name='eliminar_mensaje'),
    path('inicio-estudiante/', views.inicio_estudiante, name='inicio_estudiante'),
]

