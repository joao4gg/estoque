import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from AmoxProject.master import custom_query
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


def search_menu_notification(request):
    if request.user.is_authenticated:
        query = custom_query(f'''
                    select count(id) as qtd from AmoxProject_itemamox where name is null;
                ''')

        json_list = json.dumps({'value': query[0].get('qtd')})
        return HttpResponse(json_list)
    else:
        return redirect('index')
