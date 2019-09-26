from django.db import models


class Cadastro_lote(models.Model):
    Lote_numero = models.CharField(
        'Numero do lote',
        max_length=50
    )

    Qtd_placa = models.IntegerField(
        'Quantidade de placa',
        default=1
    )

    Ativo = models.BooleanField(
        'Lote Ativo',
        default=True
    )
    
    def __str__(self):
        return self.Lote_numero
    

    class Meta:
        db_table = 'CADASTRO_LOTE'
        constraints = [
            models.UniqueConstraint(fields=['Lote_numero'], name="Constraint_lote")
        ]