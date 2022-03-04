import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from AmoxProject.models.item_amox import ItemAmox


def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            qtd_itens = ItemAmox.objects.filter().count()
            qtd_em_estoque = ItemAmox.objects.filter(available=True).count()
            qtd_fora_estoque = ItemAmox.objects.filter(available=False).count()
            dados = {
                'user': request.user,
                'qtd_itens': qtd_itens,
                'qtd_itens_em_estoque': qtd_em_estoque,
                'qtd_itens_fora_estoque': qtd_fora_estoque
            }
            return render(request, 'index.html', dados)
        else:
            return render(request, 'user/login.html')
