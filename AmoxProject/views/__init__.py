import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from AmoxProject.master import custom_query
from AmoxProject.models.item_estoque import ItemEstoque


def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            qtd_itens = ItemEstoque.objects.filter().count()
            qtd_users = User.objects.filter(available=True).count()
            dados = {
                'user': request.user,
                'qtd_itens': qtd_itens,
                'qtd_users': qtd_users
            }
            return render(request, 'index.html', dados)
        else:
            return render(request, 'user/login.html')


def search_menu_notification(request):
    if request.user.is_authenticated:
        query = custom_query(f'''
                    select count(id) as qtd from AmoxProject_itemestoque where name is null;
                ''')

        json_list = json.dumps({'value': query[0].get('qtd')})
        return HttpResponse(json_list)
    else:
        return redirect('index')
