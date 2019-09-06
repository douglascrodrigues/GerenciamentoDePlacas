from django.contrib import admin
from testes.models import Menu_testes


class TestesAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Caminho')



admin.site.register(Menu_testes, TestesAdmin)

