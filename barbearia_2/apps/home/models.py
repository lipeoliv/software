import uuid
from django.db import models
from apps.authentication.models import User

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
    ('CS', 'Corte Social'),
    ('CU', 'Corte Undercut'),
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


class Address(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid.uuid4, editable=False)
    zip = models.IntegerField('CEP')
    public_place = models.CharField('Logradouro', max_length=50)
    neighborhood = models.CharField('Bairro', max_length=100)
    city = models.CharField('Cidade', max_length=50)
    state = models.CharField('Estado', max_length=2, choices=ESTADOS)
    complement = models.CharField('Complemento', max_length=2)
    number = models.IntegerField('Numero')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.public_place + ' ' + self.zip


class Barbershop(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid.uuid4, editable=False)
    cnpj = models.CharField(max_length=14)
    register_date = models.DateField('Data de nascimento', auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address


#galeria da barbearia com fotos de clientes (os cortes) e fotos da infraestrutura
class BarbershopImage(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid.uuid4, editable=False)
    filename = models.CharField(max_length=255)
    barbershop = models.ForeignKey(Barbershop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


# poder filtrar por barbearias que disponibilizam determinado serviço
# o barbeiro poderá cadastrar quais serviços ele disponibiliza em seu estabelecimento
# ele escolherá o serviço e dirá quanto que ele cobrará na sua barbearia
class Service(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Nome', max_length=4, choices=TIPOS_SERVICOS)
    price = models.DecimalField('Preço', max_digits=5, decimal_places=2)
    estimated_time = models.IntegerField('Tempo Estimado') # Em minutos
    barbeshop = models.ForeignKey(Barbershop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid.uuid4, editable=False)
    appointed_in = models.DateField('Reservado em', auto_now_add=True) 
    appointed_for = models.DateField('Reservado para') 
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    barbershop = models.ForeignKey(Barbershop, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} @ {}'.format(self.client, self.service, self.barbershop)


# Cartões e afins
class CreditCard(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.CharField('Portador', max_length=100)
    number = models.IntegerField('Número do cartão')
    valid_until = models.CharField('Válidade', max_length=20)
    cvv = models.IntegerField('Código de verificação')
    # adicionar bandeira

    def __str__(self):
        return self.number[-4:] # ultimos 4 dígitos