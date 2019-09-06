from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def requisicao(request): 
    return render(request, "requisicao/requisicao.html")