from django.shortcuts import render, redirect

def pagina_principal(request):
    return render(request, 'pagina_principal.html')