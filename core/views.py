from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from usuarios.forms import UsuarioForm

@login_required(login_url='inicio')
def index(requests):
    form = UsuarioForm
    titulo= 'Bienvenido'
    context={
        'titulo':titulo,
        'form':form
        }
    print(titulo)
    return render(requests, 'index.html', context)
    

def salir(request):
    logout(request)
    return redirect('inicio')

def formato(request):
    return render(request,'formato.html')

