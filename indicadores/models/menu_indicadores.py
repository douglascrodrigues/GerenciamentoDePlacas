from django.db import models

class Menu_indicadores(models.Model):
    Nome = models.CharField(
        'Nome',
        max_length=120
    )
    
    Caminho = models.CharField(
        'Caminho',
        max_length=199,
        unique=True
    )
   
    def __str__(self):
        return self.Nome

    class Meta:
        db_table = 'MENU_INDICADORES'