# Generated by Django 2.2.4 on 2019-08-31 06:21

import contas.models.usuario
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministradorUsuario',
            fields=[
            ],
            options={
                'verbose_name': 'administrador',
                'verbose_name_plural': 'administradores',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('contas.usuario',),
            managers=[
                ('objects', contas.models.usuario.UsuarioManager()),
            ],
        ),
    ]