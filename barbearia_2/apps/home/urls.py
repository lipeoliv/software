from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Agendamentos (Cliente e barbeiro)
    path('agendamentos/', views.appointments, name='appointments'),

    # Barbearias
    path('barbearias', views.barbershops, name='barbershops'),
    path('barbearia_detalhes/<uuid:barbershop_id>', views.barbershop_detail, name='barbershop_detail'),
    path('editar_barbearia/<uuid:barbershop_id>', views.barbershop_edit, name='barbershop_edit'),
    path('nova_barbearia/', views.become_barber, name='become_barber'),
    path('nova_barbearia_2/', views.become_barber_2, name='become_barber_2'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

]
