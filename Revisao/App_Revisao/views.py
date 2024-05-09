from django.shortcuts import render

from .models import Pessoas

def abre_index(request):
    return render(request, 'index.html')

def cadastrar_pessoa(request):
    if (request.method == 'POST'):
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        grava_cadastro = Pessoas (
            nome = nome,
            idade = idade
        )
        grava_cadastro.save()

        
        pessoas = Pessoas.objects.all()
        mensagem = (f'Dados do formulário {nome} {idade}')
        

    return render(request, 'index.html', {'mensagem': mensagem, 'pessoas': pessoas, 'nome': nome, 'idade':idade})