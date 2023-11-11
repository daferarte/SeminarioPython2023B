from django.urls import path
from . import views

urlpatterns = [
    path('agregar',views.agregar, name='agregar_recolector'),
    path('mostrar',views.mostrar, name='mostrar_recolector'),
    path('ver/<int:pk>',views.editar, name='ver_recolector'),
    path('eliminar/<int:pk>',views.eliminar, name='eliminar_recolector'),
]
