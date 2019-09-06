from django.db import models

# Create your models here.
class Menu_testes(models.Model):
    
    Nome = models.CharField(
        'Nome',
        max_length=120
    )
    
    Caminho = models.CharField(
        'Caminho',
        max_length=200,
        unique=True
    )

    def __str__(self):
        return self.Nome

   
    class Meta:
        db_table = 'MENU_TESTES'

