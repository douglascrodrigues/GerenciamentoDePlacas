from django.contrib import admin
from indicadores.models import Menu_indicadores

class IndicadoresAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Caminho')

admin.site.register(Menu_indicadores, IndicadoresAdmin)

