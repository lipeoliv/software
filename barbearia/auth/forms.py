from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username', 
            'password1', 
            'password2',
            'email',  
            'cpf',
            'nome', 
            'data_nascimento',
        ]


