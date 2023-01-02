from django.urls import path

# Autenticação
from .views import login, cadastro

urlpatterns = [
    path('login/', login, name='auth_login'),
    path('registrar/', cadastro, name='auth_registro'),
] 