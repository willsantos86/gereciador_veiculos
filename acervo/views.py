from django.shortcuts import render, redirect
from .forms import *

#Cadastrar carros:
def cadastrar(request):
    
    if request.method == 'POST':
        form = CadastrarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('acervo:cadastrar')
    
    else:
        form = CadastrarForm()

    context = {'form': form }

    return render(request, 'acervo/cadastrar.html', context)

#Listar carros:
def lista(request):

    lista_carros = Carro.objects.all()

    context = {'lista_carros': lista_carros}

    return render(request, 'acervo/lista.html', context)


def editar(request, pk):
    carro = Carro.objects.get(id=pk)
    form = CadastrarForm(instance= carro )
    context = {'form': form}

    if request.method=='POST':
        form = CadastrarForm(request.POST, instance= carro)

        if form.is_valid():
            form.save()
            return redirect('acervo:lista')
    return render(request, 'acervo/editar.html', context)


def deletar(request, pk):
    carro = Carro.objects.get(id=pk)
    context = {'carro': carro}
    
    if request.method=='POST':
        carro.delete()
        return redirect('acervo:lista')
    return render(request, 'acervo/deletar.html', context)
    
