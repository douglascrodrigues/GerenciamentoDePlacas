from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from contas.models import Administrador, Requisitor, Supervisor, Tester, Usuario


'''
ADMINISTRADOR
'''
def testa_administrador(user):
    return user.tipo == 'A'

@login_required
@user_passes_test(testa_administrador)
def home_administrador(request):
    admin = Administrador.objects.filter(usuario=request.user)[0]
    context = {'admin': admin}
    return render(request, 'restrito/index_administrador.html', context)


'''
REQUISITOR
'''
def testa_requisitor(user):
    return user.tipo == 'R'

@login_required
@user_passes_test(testa_requisitor)
def home_requisitor(request):
    req = Requisitor.objects.filter(usuario=request.user)[0]
    context = {'req': req}
    return render(request, 'restrito/index_requisitor.html', context)


'''
SUPERVISOR
'''
def testa_supervisor(user):
    return user.tipo == 'S'

@login_required
@user_passes_test(testa_supervisor)
def home_supervisor(request):
    sup = Supervisor.objects.filter(usuario=request.user)[0]
    context = {'sup': sup}
    return render(request, 'restrito/index_supervisor.html', context)


'''
TESTER
'''
def testa_tester(user):
    return user.tipo == 'T'

@login_required
@user_passes_test(testa_tester)
def home_tester(request):
    test = Tester.objects.filter(usuario=request.user)[0]
    context = {'test': test} 
    return render(request, 'restrito/index_tester.html', context)