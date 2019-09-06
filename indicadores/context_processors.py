from indicadores.models import Menu_indicadores

def menu_indicadores(requets):
    return {
        "Menu_indicadores": Menu_indicadores.objects.all()
    }
    