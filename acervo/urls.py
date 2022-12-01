
from django.urls import path
from .views import *

app_name = 'acervo'

urlpatterns = [
    path('deletar/<int:pk>/', deletar, name='deletar'),
    path('editar/<int:pk>/', editar, name='editar'),
    path('lista/', lista, name='lista'),
    path('cadastrar/', cadastrar, name='cadastrar'),
]
