from django.shortcuts import render, get_object_or_404
from placas.models import Menu_placas, Modelo_placas, Cadastro_placas
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ModeloForm, PlacaForm
from django import forms


@login_required
def cadastrar_modelo(request):
    list_modelo = Modelo_placas.objects.all()
    context = {
        "form": ModeloForm,
        "list_modelo": list_modelo
    }
    if request.method == "POST":
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()    
    return render(request, "placas/cadastrar-modelo.html", context)


@login_required
def cadastrar_placa(request):
    list_placa = Cadastro_placas.objects.all()
    context = {
        "form": PlacaForm,
        "list_placa": list_placa        
    }
    if request.method == "POST":
        form = PlacaForm(request.POST)
        if form.is_valid():
            form.save()      
    return render(request, "placas/cadastrar-placa.html", context)        
    


