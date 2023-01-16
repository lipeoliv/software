from django.forms import ModelForm
from django.forms import CharField, TextInput, IntegerField, NumberInput, DateField, DateInput
from django.forms import ModelChoiceField, Select, TimeField, TimeInput, ChoiceField, ClearableFileInput

from .models import Address, Service, CreditCard, Barbershop, BarbershopImage, Appointment
from .models import STATES

class AddressForm(ModelForm):
    zip = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Apenas números",
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
    state = ChoiceField(
        choices=STATES,
        widget=Select(
            attrs={
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
    name = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Nome do estabelecimento",
                "class": "form-control"
            }
        )
    ) 
    cnpj = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Apenas números",
                "class": "form-control",
                "maxlength": 14,
            }
        )
    )  
    opening_hour = TimeField(
        widget=TimeInput(
            attrs={
                "placeholder": "Hora de abertura",
                "class": "form-control",
                "type": "time"
            }
        )
    )
    closing_hour = TimeField(
        widget=TimeInput(
            attrs={
                "placeholder": "Hora de fechamento",
                "class": "form-control",
                "type": "time"
            }
        )
    )
    # O endereço será um form de endereço no template
    # as fotos será um form no template
    # o proprietário será o id do próprio usuário
    class Meta:  
        model = Barbershop  
        fields = [
            'name',
            'cnpj',
            'opening_hour',
            'closing_hour',
        ]  


class BarbershopImageForm(ModelForm):
    # estudar como fazer upload de varias images de uma vez
    class Meta:
        model = BarbershopImage
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(
                attrs={
                    'accept': ".png, .jpg, .jpeg",
                    'multiple': True,
                    'class': 'form-control',
                }
            ),
        }


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
            'appointed_for',
            'service',
        ] 


class CreditCardForm(ModelForm):  
    class Meta:  
        model = CreditCard  
        fields = [
            'owner',
            'number',
            'valid_until',
            'cvv'
        ] 
