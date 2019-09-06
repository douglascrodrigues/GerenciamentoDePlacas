from placas.models import Menu_placas

def menu_placas(requets):
    return {
        "Menu_placas": Menu_placas.objects.all()
    }