# Generated by Django 4.0.5 on 2023-01-02 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barbearia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='Data de nascimento')),
            ],
        ),
        migrations.CreateModel(
            name='CartaoCredito',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('portador', models.CharField(max_length=100, verbose_name='Portador')),
                ('numero', models.IntegerField(verbose_name='Número do cartão')),
                ('validade', models.CharField(max_length=20, verbose_name='Válidade')),
                ('cvv', models.IntegerField(verbose_name='Código de verificação')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('nome', models.CharField(choices=[('CS', 'Corte social'), ('CN', 'Corte Navalhado'), ('CP', 'Corte Pigmentado'), ('CB', 'Corte + Barba'), ('CL', 'Corte + Luzes'), ('CA', 'Corte + Alisamento'), ('LZ', 'Luzes'), ('DS', 'Desenho'), ('BR', 'Barba'), ('BP', 'Barba Pigmentada'), ('PZ', 'Pezinho'), ('SB', 'Sobrancelha'), ('MF', 'Massagem Facial'), ('MC', 'Massagem Corporal'), ('LP', 'Limpeza de Pele'), ('MN', 'Manicure'), ('PD', 'Pedicure')], max_length=4, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('tempo_estimado', models.IntegerField(verbose_name='Tempo Estimado')),
            ],
        ),
        migrations.CreateModel(
            name='ImagemBarbearia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('nome_arquivo', models.CharField(max_length=255)),
                ('imagem', models.ImageField(upload_to='images/')),
                ('barbearia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.barbearia')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('cep', models.IntegerField(verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=50, verbose_name='Logradouro')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='Estado')),
                ('complemento', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='Complemento')),
                ('numero', models.IntegerField(verbose_name='Numero')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='barbearia',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.endereco'),
        ),
        migrations.AddField(
            model_name='barbearia',
            name='proprietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='barbearia',
            name='servicos',
            field=models.ManyToManyField(related_name='barbearias', to='core.servico'),
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='Cadastrado em')),
                ('data_reserva', models.DateField(verbose_name='Data reservada')),
                ('barbearia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.barbearia')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.servico')),
            ],
        ),
    ]
