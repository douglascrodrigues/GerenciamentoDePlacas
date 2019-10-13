from django.db import models
from placas.models import Modelo_placas
from datetime import date, datetime

class Cadastro_requisicao(models.Model):
    Modelo = models.ForeignKey(
        'placas.modelo_placas', 
        related_name='requisicao_placas_modelo',
        on_delete = models.PROTECT,
        null = True,
        limit_choices_to= {'Ativo': True} #Limita somente a modelos ativos
    )
    
    Quantidade = models.IntegerField(
        'Quantidade de placas'
    )

    Descricao = models.CharField(
        'Descrição da Requisição',
        max_length=250
    )

    Data_Requisicao = models.DateTimeField(
        'Data da Requisição',
        default=datetime.now()
    )

    
    def __str__(self):
        pass #return self.Lote_numero
    

    class Meta:
        db_table = 'CADASTRO_REQUISICAO'
        constraints = [
            models.UniqueConstraint(fields=['Lote_numero'], name="Constraint_lote")
        ]