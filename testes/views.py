from django.shortcuts import render, get_object_or_404
from testes.models import Menu_testes

def testes(request, caminho):
    teste = get_object_or_404(Menu_testes, Caminho = caminho)

    context = {
        "teste": teste
    }
    
    return render(request, "testes/testes.html", context)
