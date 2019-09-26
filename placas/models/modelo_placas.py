from django.db import models
from django.db.models import constraints

# Create your models here.class Menu_placas(models.Model):
class Modelo_placas(models.Model):
    Modelo = models.CharField(
        'modelo',
        max_length=120
    )
    
    Descricao = models.CharField(
        'Descrição',
        max_length=200
    )

    Ativo = models.BooleanField(
        'Modelo Ativo',
        default=True
    )

    

    def __str__(self):
        return '{} - {}'.format(self.Modelo, self.Descricao) 

    class Meta:
        db_table = 'MODELO_PLACAS'
        constraints = [
            models.UniqueConstraint(fields=['Modelo', 'Descricao'], name="Constraint_modelo")
        ]