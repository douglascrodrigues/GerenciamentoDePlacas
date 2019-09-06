from django.db import models

class Supervisor(models.Model):
    
    nome = models.CharField(
    "Nome Completo",
    max_length=155
    )

    email = models.EmailField("E-mail")

    celular = models.CharField(
        "Celular",
        max_length=11
    )

    apelido = models.CharField(
        "Apelido",
        max_length=120
    )

    usuario = models.ForeignKey(
        'contas.Usuario',
        on_delete = models.CASCADE
    )

    class Meta:
        db_table =  'SUPERVISOR'