
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', pagina_principal, name='pagina_principal'),
    path('acervo/', include('acervo.urls'), name='acervo'),
    path('admin/', admin.site.urls),
]
