from django.shortcuts import render, get_object_or_404, redirect
from placas.models import Menu_placas, Modelo_placas, Cadastro_placas, Cadastro_lote
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


def lista_placa(request):
    list_placa = Cadastro_placas.objects.all()
    context = {
        'list_placa': list_placa
    }
    return render(request, "placas/lista-placa.html", context)

@login_required
def cadastrar_placa(request):
    context = {
        "form": PlacaForm       
    }
    if request.method == "POST":
        form = PlacaForm(request.POST)
        if form.is_valid():
            form.save()      
    return render(request, "placas/cadastrar-placa.html", context)




def excluir_placa(request, id):
    placa = get_object_or_404(Cadastro_placas, id=id)
    context = {
        "placa": Cadastro_placas.objects.filter(id=id)[0]
    }
    if request.method == "POST":
        placa.delete()
        return redirect('placas:lista-placa')
    return render(request, "placas/excluir-placa.html", context)


