from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('empleados', views.empleados, name='empleados'),
    path('autos', views.autos, name='autos'),
   
    path('autos/crear', views.crear_auto, name='crear_auto'),
    path('autos/editar', views.editar_auto, name='editar_auto'),
    path('eliminar/<int:id>', views.eliminar_auto, name='eliminar_auto'),
    path('autos/editar/<int:id>', views.editar_auto, name='editar_auto'),
    
    path('usuarios/crear', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:id>', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuarios/editar/<int:id>', views.editar_usuario, name='editar_usuario'),
    
    path('empleados/crear', views.crear_empleado, name='crear_empleado'),
    path('empleado/editar', views.editar_empleado, name='editar_empleado'),
    path('eliminar_empleado/<int:id>', views.eliminar_empleado, name='eliminar_empleado'),
    path('empleados/editar/<int:id>', views.editar_empleado, name='editar_empleado'),
    
    path('paginas/contacto/', views.contacto, name='contacto'),
    path('paginas/locales/', views.locales, name='locales'),
    path('paginas/vehiculos/', views.vehiculos, name='vehiculos'),
    
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
]

