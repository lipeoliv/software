from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UsuarioForm

def login(request):
    return render(request, 'login.html') 

def autenticar(request):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def cadastro(request):
    form = UsuarioForm(request.POST or None)
    
    if form.is_valid():
        usuario = form.save()
        tipo = request.POST['tipo'] # tipo é um campo hardcoded no form
        if tipo == 'aluno':
            permissao_aluno = Permission.objects.get(codename='aluno')
            usuario.user_permissions.add(permissao_aluno)
            usuario.save()
        elif tipo == 'professor':
            permissao_professor = Permission.objects.get(codename='professor')
            usuario.user_permissions.add(permissao_professor)
            usuario.save()
        elif tipo == 'admin':
            usuario.is_superuser = True
            usuario.save()
        return redirect('login')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro.html', contexto)


def desconectar(request):
    logout(request)
    return redirect('home')