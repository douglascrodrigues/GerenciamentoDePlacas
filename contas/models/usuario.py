from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.urls import reverse


TIPOS = (
    ('R', 'Requisitor'),
    ('T', 'Tester'),
    ('S', 'Supervisor'),
    ('A', 'Administrador')

)

class UsuarioManager(UserManager):

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('Nome de usuário é obrigatório')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('tipo', 'A')
        return self._create_user(username, password, **extra_fields)

class Usuario(AbstractBaseUser):
    username = models.CharField(
        "Nome de Usuário",
        max_length=120,
        unique=True
    )

    data_expiracao = models.DateField(
        "Data Expiração",
        null=True
    )

    tipo = models.CharField(
        "Tipo de Usuário",
        max_length=1,
        choices = TIPOS
    )

    objects = UsuarioManager()

    USERNAME_FIELD =  'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.tipo == 'A'
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        if self.tipo == 'R':
            return reverse('restrito:home_requisitor')
        elif self.tipo == 'S':
            return reverse('restrito:home_supervisor')
        elif self.tipo == 'T':
            return reverse('restrito:home_tester')
        else:
            return reverse('restrito:home_administrador')


    class Meta:
        db_table = 'USUARIO'