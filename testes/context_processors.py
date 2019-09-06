from testes.models import Menu_testes

def menu_testes(requets):
    return {
        "lista_testes": Menu_testes.objects.all()
    }
