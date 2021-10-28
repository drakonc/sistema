from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear_libro, name='crear_libro'),
    path('libros/editar', views.editar_libro, name='editar_libro')
]
