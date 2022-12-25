from django.forms import ModelForm

from .models import Servico, CartaoCredito, Barbearia, ImagemBarbearia, Agendamento


class EnderecoUsuarioForm(ModelForm):
    class Meta:
        model = Endereco
        fields = [
            'cep', 
            'bairro', 
            'cidade',
            'estado',  
            'complemento',
            'numero', 
            'usuario',
        ]


class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = [
            'nome',
            'preco',
            'tempo_estimado',
        ]

class BarbeariaForm(ModelForm):  
    class Meta:  
        model = Barbearia  
        fields = [
            'data_cadastro',
            'cep',
            'logradouro',
            'numero',
            'complemento',
            'referencia',
            'bairro',
            'cidade',
            'estado',
            'servicos',
        ]  


class ImagemBarbeariaForm(ModelForm):
    class Meta:
        model = ImagemBarbearia
        fields = [
            'nome_arquivo',
            'barbearia',
            'imagem',
        ]


class AgendamentoForm(ModelForm):  
    class Meta:  
        model = Agendamento  
        fields = [
            'data_cadastro',
            'data_reserva',
            'servico',
            'cliente',
            'barbearia',
        ] 


class CartaoCreditoForm(ModelForm):  
    class Meta:  
        model = CartaoCredito  
        fields = [
            'owner',
            'number',
            'valid_until',
            'cvv'
        ] 
