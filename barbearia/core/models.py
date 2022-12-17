import uuid
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

# permissoes = slide 74+
class Usuario(AbstractUser):
    nome = models.CharField('Nome Completo', max_length=100)
    data_nascimento = models.DateField('Data de nascimento')
    cpf = models.CharField('CPF', max_length=11, unique=True)
    

    # foreign para dizer se é barbeiro

    USERNAME_FIELD = 'cpf'

class Barbearia(models.Model):
    id = models.UUIDField("Id", primary_key=True, default=uuid.uuid4, editable=False)
    data_cadastro = models.DateField('Data de nascimento', auto_now_add=True)
    cep = models.IntegerField('Cep')
    logradouro = models.CharField('Logradouro', max_length=50)
    numero = models.IntegerField('Número')
    complemento = models.CharField('Complemento', max_length=100)
    referencia = models.CharField('Referência', max_length=100)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField("Estado", max_length=2, choices=ESTADOS)

class Agendamento(models.Model):
    id = models.UUIDField("Id", primary_key=True, default=uuid.uuid4, editable=False)
    data_cadastro = models.DateField('Cadastrado em', auto_now_add=True) 
    data_reserva = models.DateField('Data reservada') 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)