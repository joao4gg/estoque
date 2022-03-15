from datetime import datetime

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect

from AmoxProject.models.item_aux import ItemAux
from AmoxProject.models.item_estoque import ItemEstoque


def buscar(request):
    if request.user.is_authenticated:
        fields = dict()
        cad_pen = False
        if request.method == 'GET':
            if 'flag' in request.GET.keys():
                cad_pen = True
                rows = ItemEstoque.objects.filter(name__isnull=True)
            else:
                rows = ItemEstoque.objects.filter()
        else:
            fields = {'busca': request.POST['busca'], 'filtro': request.POST['filtro']}
            if request.POST['busca'] != '':
                if request.POST['filtro'] == 'codigo':
                    if 'flag' in request.GET.keys():
                        cad_pen = True
                        rows = ItemEstoque.objects.filter(Q(codigo__icontains=request.POST['busca']), name__isnull=True)
                    else:
                        rows = ItemEstoque.objects.filter(Q(codigo__icontains=request.POST['busca']))
                else:
                    rows = ItemEstoque.objects.filter(Q(name__icontains=request.POST['busca']))
            else:
                rows = ItemEstoque.objects.filter()

        dados = {
            'titulo': 'Items - Buscar',
            'rows': rows,
            'fields': fields,
            'cad_pen': cad_pen
        }
        return render(request, 'item/buscar.html', dados)
    else:
        return redirect('/admin/')


def inserir(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            dados = {
                'flag': 0,
            }
            return render(request, 'item/cadastro.html', dados)

        else:
            ver_item = ItemEstoque.objects.filter(name__exact=request.POST['name'], codigo__exact=request.POST['codigo'])
            if ver_item is not None:
                messages.warning(request, 'Produto Já Cadastrado!')
                return redirect('inserir_item')

            else:
                item_estoque = ItemEstoque.objects.create()
                item_estoque.name = request.POST['name']
                item_estoque.codigo = request.POST['codigo']
                item_estoque.id_und_id = request.POST['id_und_id']
                item_estoque.qtde = request.POST['qtde']
                item_estoque.save()

                if item_estoque is not None:
                    item_aux = ItemAux.objects.create()
                    item_aux.id_user = request.user
                    item_aux.id_item = item_estoque
                    item_aux.data = datetime.now()
                    item_aux.save()

                    messages.success(request, 'Produto Cadastrado com Sucesso!')
                    return redirect('buscar_item')
    else:
        return redirect('/admin/')


def editar(request, id):
    if request.user.is_authenticated:
        item = ItemEstoque.objects.filter(id=id).last()
        if item is not None:
            dados = {
                'model': item,
            }
            return render(request, 'item/cadastro.html', dados)
    else:
        return redirect('/admin/')


def atualizar(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            item = ItemEstoque.objects.filter(id=request.POST['id']).last()
            if item is not None:
                item.name = request.POST['name']
                item.codigo = request.POST['codigo']
                item.id_und_id = request.POST['id_und_id']
                item.qtde = request.POST['qtde']
                item.save()

                messages.success(request, 'Alterações Gravadas com Sucesso!')
                return redirect('buscar_item')
        else:
            return redirect('index')
    else:
        return redirect('index')
