from django.db import models
from django.contrib.auth.models import AbstractUser

ESTADOS = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)


class Usuario(AbstractUser):
    cpf = models.CharField('CPF', max_length=11, unique=True)
    nome = models.CharField('Nome Completo', max_length=100)
    data_nascimento = models.DateField('Data de nascimento')
    
    USERNAME_FIELD = 'cpf'

    class Meta:
        permissions = [
            ('Admin', 'Permissao de administrador'),
            ('Barbeiro', 'Permissao de barbeiro'),
            ('Usuario', 'Permissao de usuario comum'),
        ]



