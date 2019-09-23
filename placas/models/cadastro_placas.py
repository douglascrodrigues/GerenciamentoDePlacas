from django.db import models

# Create your models here.class Menu_placas(models.Model):
class Cadastro_placas(models.Model):
    Numero_serie = models.CharField(
        'Número de série',
        max_length=120
    )
    
    Modelo = models.ForeignKey(
        'placas.modelo_placas', 
        related_name='modelo_placas_modelo',
        on_delete = models.PROTECT,
        null = True
    )

    Revisao_lm = models.IntegerField(
        'Revisao LM'
    )

    Lote_numero = models.ForeignKey(
        'placas.cadastro_lote',
        related_name='numero_lote',
        on_delete = models.PROTECT
    )

    Observacao = models.TextField(
        'Observação',
        blank=True
    )
   
    def __str__(self):
        return self.Numero_serie

    class Meta:
        db_table = 'CADASTRO_PLACAS'
        constraints = [
            models.UniqueConstraint(fields=['Numero_serie'], name="Constraint_placas")
        ]



