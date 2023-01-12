from django.db import models
from django.contrib.auth.models import AbstractUser

# Endereço será necessário apenas para as barbearias
class User(AbstractUser):
    cpf = models.CharField('CPF', max_length=11, unique=True)
    name = models.CharField('Nome Completo', max_length=100)
    birth = models.DateField('Data de nascimento')
    
    USERNAME_FIELD = 'cpf'

    class Meta:
        permissions = [
            ('Admin', 'Permissao de administrador'),
            ('Barbeiro', 'Permissao de barbeiro'),
            ('Usuario', 'Permissao de usuario comum'),
        ]

    def __str__(self):
        return '{} ({})'.format(self.nome, self.cpf)


