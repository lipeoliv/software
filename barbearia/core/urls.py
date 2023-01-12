from django.urls import path


# Dados do usuário
from .views import index, dados_usuario, agendamentos, servicos, add_servico

# Endereços
from .views import create_endereco, update_endereco, destroy_endereco

# Cartões
from .views import create_cartao, update_cartao, destroy_cartao

# Produtos
from .views import show_servicos, create_servico, update_servico, destroy_servico

# name='nomeApp_nomeUrl'
urlpatterns = [
    path('', index, name='index'),
    path('meusdados/', dados_usuario, name='dados_usuario'),
    path('agendamentos/', agendamentos, name='agendamentos'),
    
    # Se o usuario for barbeiro, libera essa opção
    path('servicos/', servicos, name='servicos'),

    # Endereços
    path('enderecos/', create_endereco, name='enderecos_usuario'),
    path('enderecos/atualizar/<uuid:id>', update_endereco, name='update_endereco'),
    path('enderecos/apagar/<uuid:id>', destroy_endereco, name='destroy_endereco'),

    # Cartões
    path('meuscartoes/', create_cartao, name='cartoes_usuario'),
    path('meuscartoes/atualizar/<uuid:id>', update_cartao, name='update_cartao'),
    path('meuscartoes/apagar/<uuid:id>', destroy_cartao, name='destroy_cartao'),

    # Produtos
    path('meusprodutos/', show_servicos, name='servicos_usuario'),
    path('meusprodutos/adicionar/', create_servico, name='create_servico'),
    #path('meusprodutos/detalhar/<uuid:id>', product_detail, name='product_detail'),
    path('meusprodutos/atualizar/<uuid:id>', update_servico, name='update_servico'),
    path('meusprodutos/apagar/<uuid:id>', destroy_servico, name='destroy_servico'),


] 
'''
    
'''