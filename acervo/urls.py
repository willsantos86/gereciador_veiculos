
from django.urls import path
from .views import *

app_name = 'acervo'

urlpatterns = [
    path('lista/', lista, name='lista'),
    path('cadastrar/', cadastrar, name='cadastrar'),
]
