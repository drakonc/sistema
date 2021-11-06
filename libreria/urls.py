from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear_libro, name='crear_libro'),
    path('libros/editar/<int:id>', views.editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:id>',views.eliminar_libro, name='eliminar_libro')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)