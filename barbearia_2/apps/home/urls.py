from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Agendamentos (Cliente e barbeiro)
    path('agendamentos/', views.appointments, name='appointments'),

    # Barbearias
    path('barbearias/', views.barbershops, name='barbershops'),
    path('barbearia/<uuid:barbershop_id>/', views.barbershop_detail, name='barbershop_detail'),
    path('barbearia/<uuid:barbershop_id>/servicos/', views.barbershop_services, name='barbershop_services'),
    path('editar_barbearia/<uuid:barbershop_id>/', views.barbershop_edit, name='barbershop_edit'),
    path('editar_barbearia_endereco/<uuid:barbershop_id>/', views.barbershop_edit_address, name='barbershop_edit_address'),
    path('editar_barbearia_servicos/<uuid:service_id>/', views.barbershop_edit_services, name='barbershop_edit_services'),
    path('nova_barbearia/', views.become_barber, name='become_barber'),
    path('nova_barbearia_endereco/', views.become_barber_2, name='become_barber_2'),
    
    # Usuário comum
    path('index/', views.index, name='index'),
    path('agendar/<uuid:barbershop_id>/', views.make_appointment, name='make_appointment'),
    path('tables/', views.tables, name='tables'),
    path('profile/', views.profile, name='profile'),
    path('billing/', views.billing, name='billing'),
    path('promotions/', views.promotions, name='promotions'),
    path('arrangements/', views.arrangements, name='arrangements')
    

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

]
