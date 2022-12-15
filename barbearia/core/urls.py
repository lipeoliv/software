from django.urls import path
from .views import index, user_data, orders, products, addresses, add_product

# Endereços
from .views import create_address, update_address, destroy_address

# Cartões
from .views import create_credit_card, update_card, destroy_card

# Produtos
from .views import show_products, create_product, update_product, destroy_product

urlpatterns = [
    path('', index, name='user_index'),
    path('meusdados/', user_data, name='user_data'),
    path('pedidos/', orders, name='user_orders'),
    #path('meusprodutos/', products, name='user_products'),
    #path('meusprodutos/adicionarproduto/', add_product, name='user_add_product'),
    #path('enderecos/', addresses, name='user_addresses'),

    # Endereços
    path('enderecos/', create_address, name='user_addresses'),
    path('enderecos/atualizar/<uuid:id>', update_address, name='update_address'),
    path('enderecos/apagar/<uuid:id>', destroy_address, name='destroy_address'),

    # Cartões
    path('meuscartoes/', create_credit_card, name='user_cards'),
    path('meuscartoes/atualizar/<uuid:id>', update_card, name='update_card'),
    path('meuscartoes/apagar/<uuid:id>', destroy_card, name='destroy_card'),

    # Produtos
    path('meusprodutos/', show_products, name='user_products'),
    path('meusprodutos/adicionar/', create_product, name='add_product'),
    #path('meusprodutos/detalhar/<uuid:id>', product_detail, name='product_detail'),
    path('meusprodutos/atualizar/<uuid:id>', update_product, name='update_product'),
    path('meusprodutos/apagar/<uuid:id>', destroy_product, name='destroy_product'),

] 
