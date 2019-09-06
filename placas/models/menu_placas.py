from django.db import models


# Create your models here.class Menu_placas(models.Model):
class Menu_placas(models.Model):
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
        db_table = 'MENU_PLACAS'


        


