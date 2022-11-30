from django.forms import ModelForm
from .models import *

class CadastrarForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['marca', 'modelo', 'versao', 'ano_fabricacao', 'chassis']
