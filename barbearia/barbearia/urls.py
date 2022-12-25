from django.urls import path, include

# Importação das urls
from core import urls as core_urls
from auth import urls as auth_urls

urlpatterns = [
    # Urls da aplicação principal
    path('', include(core_urls)),
    
    # Urls de autenticação
    path('', include(auth_urls)),
] 
