from django.urls import path
from . import views

urlpatterns = [
    path('', views.abre_index, name = 'abre_index'),
    path('cadastrar_pessoa', views.cadastrar_pessoa, name='cadastrar_pessoa')
]
