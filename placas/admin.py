from django.contrib import admin
from placas.models import  Menu_placas, Cadastro_lote, Cadastro_placas, Modelo_placas


class MenuPlacasAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Caminho')


class CadastroPlacasAdmin(admin.ModelAdmin):
    list_display = ('Modelo', )

class ModeloPlacasAdmin(admin.ModelAdmin):
    list_display = ('Modelo', 'Descricao')

class LotePlacasAdmin(admin.ModelAdmin):
    list_display = ('Lote_numero',)

admin.site.register(Menu_placas, MenuPlacasAdmin)
admin.site.register(Cadastro_placas, CadastroPlacasAdmin)
admin.site.register(Cadastro_lote, LotePlacasAdmin)
admin.site.register(Modelo_placas, ModeloPlacasAdmin)