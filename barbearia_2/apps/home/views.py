from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
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
    print("acessando Enderecoes")
    if request.method == "POST":
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
        "enderecos": enderecos,
        "form": form
    }

    return render(request, 'enderecos.html', context)


def update_endereco(request, id):  
    endereco = Address.objects.get(id=id)  
    form = EnderecoUsuarioForm(request.POST, instance=endereco)  
    
    if form.is_valid():  
        form.save()  
        return redirect("user_Enderecoes")  
    
    context = {
        "endereco": Address,
        "enderecos": Address.objects.all(),
        "form": form
    }
    return render(request, 'endereco_edit.html', context)  


def destroy_endereco(request, id):  
    endereco = Address.objects.get(id=id)  
    endereco.delete()  
    return redirect("user_enderecos")  


# Credit card views
def create_cartao(request):
    if request.method == "POST":
        
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
        "cartoes": cartoes,
        "form": form
    }

    return render(request, 'cards.html', context)


def update_cartao(request, id):  
    cartao = CreditCard.objects.get(id=id)  
    form = CartaoCreditoForm(request.POST, instance=cartao)  
    
    if form.is_valid():  
        form.save()  
        return redirect("user_cards")  
    
    context = {
        "cartao": cartao,
        "cartoes": CreditCard.objects.all(),
        "form": form
    }
    return render(request, 'card_edit.html', context)  


def destroy_cartao(request, id):  
    cartao = CreditCard.objects.get(id=id)  
    cartao.delete()  
    return redirect("user_cards")  


# Servico views
def servicos(request):
    return render(request, 'meus_servicos.html')


def show_servicos(request):
    servicos = Service.objects.all()
    context = {
        "servicos": servicos
    }
    return render(request, 'servicos_show.html', context)


def add_servico(request):
    return render(request, 'add_servico.html')


def create_servico(request):
    if request.method == "POST":
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
        "form": form
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

        return redirect("user_Servicos")  
    
    context = {
        "servico": servico,
        "form": form,
        #"images": images
    }
    return render(request, 'Servico_edit.html', context)  


def destroy_servico(request, id):  
    servico = Service.objects.get(id=id)  
    servico.delete()  
    return redirect("user_Servicos") 
    '''