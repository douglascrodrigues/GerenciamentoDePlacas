from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    context = {
        "titulo":"GenesisQ"

    }
    return render(request, "index.html", context)


def entrar(request):
    context = {}
    if request.POST:
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        usuario = authenticate(username=usuario, password=senha)
        if usuario:
            login(request, usuario)
            return redirect(usuario.get_absolute_url())
        else:
            messages.error(request, 'Usuário ou senha incorretos!')
    return render(request, 'entrar.html', context)

def sair(request):
    logout(request)
    return redirect('core:home')

def admin(request):
    return redirect('core:admin')
