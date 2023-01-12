from django.urls import path

# Autenticação
from .views import login, cadastro

urlpatterns = [
    path('login/', login, name='login'),
    path('registrar/', cadastro, name='registro'),
] 