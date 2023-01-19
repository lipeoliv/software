from django import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Modelos
from .models import User, Barbershop, BarbershopImage, Address

# Forms
from .forms import BarbershopForm, BarbershopImageForm, AddressForm

@login_required(login_url='/login/')
def index(request):
    context = {'segment': 'index'}
    return render(request, 'home/client_index.html', context)


@login_required(login_url='/login/')
def appointments(request):
    context = {'segment': 'appointments'}
    return render(request, 'home/index.html', context)


# Barbearias
@ login_required(login_url='/login/')
def barbershops(request):
    context = {'segment': 'barbershops' }
    
    # Barbearias do usuario
    if request.user.has_perm('authentication.barber_perm'):
        user_barbershops = Barbershop.objects.filter(owner=request.user)
        for barbershop in user_barbershops:
            # Seleciona a primeira imagem de cada barbearia
            barbershop.main_img = BarbershopImage.objects.filter(barbershop=barbershop).last()

        context['user_barbershops'] = user_barbershops
    return render(request, 'home/barbershops.html', context)


@login_required(login_url='/login/')
def barbershop_detail(request, barbershop_id):
    barbershop = Barbershop.objects.get(id=barbershop_id)
    barbershop_images = BarbershopImage.objects.filter(barbershop=barbershop)
    context = {
        'segment': 'become_barber',
        'barbershop': barbershop,
        'barbershop_images': barbershop_images,
        'barbershop_main_image': barbershop_images[0]
    }
    return render(request, 'home/barber/barbershop_detail.html', context)


@login_required(login_url='/login/')
def become_barber(request):
    # Se ja tem o cadastro de barbearia em andamento, redireciona para become_barber_2
    current_barbershop = Barbershop.objects.filter(owner=request.user).filter(completed=False)
    if current_barbershop:
        return redirect('become_barber_2')

    user_msg = ''
    if request.method == 'POST':
        form = BarbershopForm(request.POST)
        form2 = BarbershopImageForm(request.POST, request.FILES)
        images = request.FILES.getlist('image')

        if form.is_valid() and form2.is_valid():
            barbershop = form.save(commit=False)
            barbershop.owner = request.user
            barbershop.save()

            print(barbershop)
            for image in images:
                BarbershopImage.objects.create(barbershop=barbershop, image=image)
                print('guardou imagem')

            # Add permissao de barbeiro ao usuario
            barber_permission = Permission.objects.get(codename='barber_perm')
            request.user.user_permissions.add(barber_permission)
            return redirect('become_barber_2')
        else: 
            user_msg = form.errors.as_text() + ' ' + form2.errors.as_text()
    else:
        form = BarbershopForm()
        form_2 = BarbershopImageForm()
        user_msg = 'Preencha os dados do seu negócio'
     
    context = {
        'segment': 'become_barber',
        'form': form,
        'form_2': form_2,
        'msg': user_msg,
    }

    return render(request, 'home/barber/become_barber.html', context)


# Cadastro de barbearia
@login_required(login_url='/login/')
@permission_required('authentication.barber_perm')
def become_barber_2(request):
    last_barbershop = Barbershop.objects.filter(owner=request.user).filter(completed=False).first()
    user_msg = ''

    # Não iniciou o cadastro de nenhuma barbearia
    if not last_barbershop: 
        return redirect('become_barber')

    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.barbershop = last_barbershop
            address.save()
            
            # Altera o estado do cadastro da barbearia
            last_barbershop.completed = True
            last_barbershop.save()
            return redirect('barbershops')
        else: 
            for error in form.errors.values():
                user_msg += error
    else:
        form = AddressForm()
     
    context = {
        'segment': 'become_barber',
        'last_barbershop': last_barbershop,
        'form': form,
        'msg': user_msg,
    }

    return render(request, 'home/barber/become_barber_2.html', context)


@login_required(login_url='/login/')
@permission_required('authentication.barber_perm')
def barbershop_edit(request, barbershop_id):
    barbershop = Barbershop.objects.get(id=barbershop_id)  
    if barbershop.owner != request.user: # Se a barbearia não pertencer ao usuario 
        redirect('barbershops')

    form = BarbershopForm(request.POST or None, instance=barbershop) 
    address = Address.objects.get(barbershop_id=barbershop.id)
    address_form = AddressForm(request.POST or None, instance=address)
    
    if form.is_valid() and address_form.is_valid():  
        form.save()  
        address_form.save() 
        return redirect('barbershops')  
    
    context = {
        'barbershop': barbershop,
        'form': form,
        'form_2': address_form,
    }
    return render(request, 'home/barber/barbershop_edit.html', context)  


@login_required(login_url='/login/')
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
'''

from django.shortcuts import render, redirect
from .forms import EnderecoUsuarioForm, CartaoCreditoForm, ServicoForm
from .models import Address, CreditCard, Service#, ServicoImage      

def index(request):
    return render(request, 'user.html')

def dados_usuario(request):
    return render(request, 'dados_pessoais.html')

def agendamentos(request):
    return render(request, 'agendamentos.html')


# Endereco views
def create_endereco(request):
    print('acessando Enderecoes')
    if request.method == 'POST':
        form = EnderecoUsuarioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('user_enderecoes')
            except:
                pass
    else:
        enderecos = Address.objects.all() 
        form = EnderecoUsuarioForm()
     
    context = {
        'enderecos': enderecos,
        'form': form
    }

    return render(request, 'enderecos.html', context)


def update_endereco(request, id):  
    endereco = Address.objects.get(id=id)  
    form = EnderecoUsuarioForm(request.POST, instance=endereco)  
    
    if form.is_valid():  
        form.save()  
        return redirect('user_Enderecoes')  
    
    context = {
        'endereco': Address,
        'enderecos': Address.objects.all(),
        'form': form
    }
    return render(request, 'endereco_edit.html', context)  


def destroy_endereco(request, id):  
    endereco = Address.objects.get(id=id)  
    endereco.delete()  
    return redirect('user_enderecos')  


# Credit card views
def create_cartao(request):
    if request.method == 'POST':
        
        form = CartaoCreditoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('user_cards')
            except:
                pass
    else:
        cartoes = CreditCard.objects.all() 
        form = CartaoCreditoForm()
     
    context = {
        'cartoes': cartoes,
        'form': form
    }

    return render(request, 'cards.html', context)


def update_cartao(request, id):  
    cartao = CreditCard.objects.get(id=id)  
    form = CartaoCreditoForm(request.POST, instance=cartao)  
    
    if form.is_valid():  
        form.save()  
        return redirect('user_cards')  
    
    context = {
        'cartao': cartao,
        'cartoes': CreditCard.objects.all(),
        'form': form
    }
    return render(request, 'card_edit.html', context)  


def destroy_cartao(request, id):  
    cartao = CreditCard.objects.get(id=id)  
    cartao.delete()  
    return redirect('user_cards')  


# Servico views
def servicos(request):
    return render(request, 'meus_servicos.html')


def show_servicos(request):
    servicos = Service.objects.all()
    context = {
        'servicos': servicos
    }
    return render(request, 'servicos_show.html', context)


def add_servico(request):
    return render(request, 'add_servico.html')


def create_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        images = request.FILES.getlist('images')
        if form.is_valid():
            try:
                new_Servico = form.save()
                #for image in images:
                    #ServicoImage.objects.create(name=image.name, Servico=new_Servico, image=image)

                return redirect('user_servicos')
            except:
                pass
    else:
        form = ServicoForm()
     
    context = {
        'form': form
    }

    return render(request, 'servico_add.html', context)


def update_servico(request, id):  
    servico = Service.objects.get(id=id)  
    form = ServicoForm(request.POST, instance=Service)
    #images = ServicoImage.objects.filter(Servico=Servico)
    #new_images = request.FILES.getlist('images') or []

    if form.is_valid():  
        form.save()
        #for image in new_images:
            #ServicoImage.objects.create(name=image.name, Servico=Servico, image=image)

        return redirect('user_Servicos')  
    
    context = {
        'servico': servico,
        'form': form,
        #'images': images
    }
    return render(request, 'Servico_edit.html', context)  


def destroy_servico(request, id):  
    servico = Service.objects.get(id=id)  
    servico.delete()  
    return redirect('user_Servicos') 
    '''