from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas' : pessoas})

def salvar(request):
    var_nome = request.POST.get('nome')
    var_email = request.POST.get('email')
    var_cidade = request.POST.get('cidade')

    Pessoa.objects.create(nome = var_nome, email = var_email, cidade = var_cidade)

    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas' : pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa" : pessoa})

def update(request, id):
    var_nome = request.POST.get('nome')
    var_email = request.POST.get('email')
    var_cidade = request.POST.get('cidade')
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = var_nome
    pessoa.email = var_email
    pessoa.cidade = var_cidade
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)