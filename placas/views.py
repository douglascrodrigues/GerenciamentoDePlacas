from django.shortcuts import render, get_object_or_404, redirect
from placas.models import Menu_placas, Modelo_placas, Cadastro_placas, Cadastro_lote
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ModeloForm, PlacaForm, LoteForm
from django import forms


### VIEWS MODELO ####

@login_required
def lista_modelo(request, id=None):
    pesquisa = request.GET.get("pesquisa", None)
    if pesquisa:
        list_modelo = Modelo_placas.objects.all()
        list_modelo = list_modelo.filter(Modelo__icontains=pesquisa) #Icontains é como se fosse um like%% do SQL
    else:
        list_modelo = Modelo_placas.objects.all()
    context = {
        'list_modelo': list_modelo
    }
    return render(request, "placas/lista-modelo.html", context)

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
def excluir_modelo(request, id):
    modelos = get_object_or_404(Modelo_placas, id=id)
    context = {
        "modelos": Modelo_placas.objects.filter(id=id)[0]
    }
    if request.method == "POST":
        modelos.delete()
        return redirect('placas:lista-modelo')
    return render(request, "placas/excluir-modelo.html", context)

@login_required
def atualiza_modelo(request, id):
    modelos = get_object_or_404(Modelo_placas, pk=id)
    form = ModeloForm(request.POST or None, request.FILES or None, instance=modelos)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        return redirect('placas:lista-modelo') 
    return render(request, "placas/cadastrar-modelo.html", context)




### VIEWS PLACA ####

@login_required
def lista_placa(request, id=None):
    pesquisa = request.GET.get("pesquisa", None)
    if pesquisa:
        list_placa = Cadastro_placas.objects.all()
        list_placa = list_placa.filter(Numero_serie__icontains=pesquisa) #Icontains é como se fosse um like%% do SQL
    else:
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



@login_required
def excluir_placa(request, id):
    placa = get_object_or_404(Cadastro_placas, id=id)
    context = {
        "placa": Cadastro_placas.objects.filter(id=id)[0]
    }
    if request.method == "POST":
        placa.delete()
        return redirect('placas:lista-placa')
    return render(request, "placas/excluir-placa.html", context)

@login_required
def atualiza_placa(request, id):
    placas = get_object_or_404(Cadastro_placas, pk=id)
    form = PlacaForm(request.POST or None, request.FILES or None, instance=placas)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        return redirect('placas:lista-placa') 
    return render(request, "placas/cadastrar-placa.html", context)



    ### VIEWS PLACA ####

@login_required
def lista_lote(request, id=None):
    pesquisa = request.GET.get("pesquisa", None)
    if pesquisa:
        list_lote = Cadastro_lote.objects.all()
        list_lote = list_lote.filter(Lote_numero__icontains=pesquisa) #Icontains é como se fosse um like%% do SQL
    else:
        list_lote = Cadastro_lote.objects.all()
    context = {
        'list_lote': list_lote
    }
    return render(request, "placas/lista-lote.html", context)


@login_required
def cadastrar_lote(request):
    context = {
        "form": LoteForm   
    }
    if request.method == "POST":
        form = LoteForm(request.POST)
        if form.is_valid():
            form.save()      
    return render(request, "placas/cadastrar-lote.html", context)

