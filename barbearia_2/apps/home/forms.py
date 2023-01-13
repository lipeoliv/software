from django.forms import ModelForm
from django.forms import CharField, TextInput, IntegerField, NumberInput, DateField, DateInput, ModelChoiceField, Select

from .models import Address, Service, CreditCard, Barbershop, BarbershopImage, Appointment


class AddressForm(ModelForm):
    zip = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "CEP",
                "class": "form-control"
            }
        )
    )
    public_place = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Logradouro",
                "class": "form-control"
            }
        )
    )
    neighborhood = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Bairro",
                "class": "form-control"
            }
        )
    )
    city = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Cidade",
                "class": "form-control"
            }
        )
    )
    state = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Estado",
                "class": "form-control"
            }
        )
    )
    complement = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Complemento",
                "class": "form-control"
            }
        )
    )
    number = IntegerField(
        widget=NumberInput(
            attrs={
                "placeholder": "Número",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Address
        fields = [
            'zip', 
            'public_place', 
            'neighborhood',
            'city',  
            'state',
            'complement', 
            'number',
        ]


class ServiceForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Nome",
                "class": "form-control"
            }
        )
    )
    price = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Preço",
                "class": "form-control"
            }
        )
    )
    estimated_time = IntegerField(
        widget=NumberInput(
            attrs={
                "placeholder": "Tempo estimado (Em minutos)",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Service
        fields = [
            'name',
            'price',
            'estimated_time',
        ]


class BarbershopForm(ModelForm):
    cnpj = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "CNPJ",
                "class": "form-control"
            }
        )
    )  
    # O endereço será um form de endereço no template
    # as fotos será um form no template
    # o proprietário será o id do próprio usuário
    class Meta:  
        model = Barbershop  
        fields = [
            'cnpj'
        ]  


class BarbershopImageForm(ModelForm):
    # estudar como fazer upload de varias images de uma vez
    class Meta:
        model = BarbershopImage
        fields = [
            'filename',
            'barbershop',
            'image',
        ]


class AppointmentForm(ModelForm):  
    appointed_in = DateField(
        widget=DateInput(
            attrs={
                "type": "date",
                "placeholder": "Reservado em",
                "class": "form-control"
            }
        )
    )
    appointed_for = DateField(
        widget=DateInput(
            attrs={
                "type": "date",
                "placeholder": "Reservado para",
                "class": "form-control"
            }
        )
    )
    service = ModelChoiceField(
        queryset=Service.objects.all(), 
        empty_label=None,
        widget=Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:  
        model = Appointment  
        fields = [
            'servico',
            'cliente',
            'barbearia',
        ] 


class CreditCardForm(ModelForm):  
    class Meta:  
        model = CreditCard  
        fields = [
            'portador',
            'numero',
            'validade',
            'cvv'
        ] 
