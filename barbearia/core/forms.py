from django.forms import ModelForm

from .models import Endereco, Servico, CartaoCredito, Barbearia, ImagemBarbearia, Agendamento


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
            'endereco',
            'proprietario',
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
            'servico',
            'cliente',
            'barbearia',
        ] 


class CartaoCreditoForm(ModelForm):  
    class Meta:  
        model = CartaoCredito  
        fields = [
            'portador',
            'numero',
            'validade',
            'cvv'
        ] 
