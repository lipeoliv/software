import uuid
from django.db import models
from auth.models import Usuario

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

TIPOS_SERVICOS = (
    ('CS', 'Corte social'),
    ('CN', 'Corte Navalhado'),
    ('CP', 'Corte Pigmentado'),
    ('CB', 'Corte + Barba'),
    ('CL', 'Corte + Luzes'),
    ('CA', 'Corte + Alisamento'),
    ('LZ', 'Luzes'),
    ('DS', 'Desenho'),
    ('BR', 'Barba'),
    ('BP', 'Barba Pigmentada'),
    ('PZ', 'Pezinho'),
    ('SB', 'Sobrancelha'),
    ('MF', 'Massagem Facial'),
    ('MC', 'Massagem Corporal'),
    ('LP', 'Limpeza de Pele'),
    ('MN', 'Manicure'),
    ('PD', 'Pedicure'),
)

class Endereco(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid.uuid4, editable=False)
    cep = models.IntegerField('CEP')
    logradouro = models.CharField('Logradouro', max_length=50)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('Estado', max_length=2, choices=ESTADOS)
    complemento = models.CharField('Complemento', max_length=2, choices=ESTADOS)
    numero = models.IntegerField('Numero')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

# poder filtrar por barbearias que disponibilizam determinado serviço
# o barbeiro poderá cadastrar quais serviços ele disponibiliza em seu estabelecimento
# ele escolherá o serviço e dirá quanto que ele cobrará na sua barbearia
class Servico(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField('Nome', max_length=4, choices=TIPOS_SERVICOS)
    preço = models.DecimalField('Preço', max_digits=5, decimal_places=2)
    tempo_estimado = models.IntegerField('Tempo Estimado') # Em minutos


#galeria da barbearia com fotos de clientes (os cortes) e fotos da infraestrutura
class Barbearia(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid.uuid4, editable=False)
    data_cadastro = models.DateField('Data de nascimento', auto_now_add=True)
    
    # Forma normal para isolar endereços
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    # Dono da barbearia
    proprietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    # serviços que podem ser ofertados pela barbearia
    servicos = models.ManyToManyField(Servico, related_name='barbearias')


class ImagemBarbearia(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid.uuid4, editable=False)
    nome_arquivo = models.CharField(max_length=255)
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='images/')


class Agendamento(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid.uuid4, editable=False)
    data_cadastro = models.DateField('Cadastrado em', auto_now_add=True) 
    data_reserva = models.DateField('Data reservada') 
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)


# Cartões e afins
class CartaoCredito(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid.uuid4, editable=False)
    portador = models.CharField('Portador', max_length=100)
    numero = models.IntegerField('Número do cartão')
    validade = models.CharField('Válidade', max_length=20)
    cvv = models.IntegerField('Código de verificação')
