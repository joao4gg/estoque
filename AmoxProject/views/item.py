from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from AmoxProject.models.item_amox import ItemAmox


def buscar(request):
    if request.user.is_authenticated:
        fields = dict()
        cad_pen = False
        if request.method == 'GET':
            if 'flag' in request.GET.keys():
                cad_pen = True
                rows = ItemAmox.objects.filter(name__isnull=True)
            else:
                rows = ItemAmox.objects.filter()
        else:
            fields = {'busca': request.POST['busca'], 'filtro': request.POST['filtro']}
            if request.POST['busca'] != '':
                if request.POST['filtro'] == 'id_rfid':
                    if 'flag' in request.GET.keys():
                        cad_pen = True
                        rows = ItemAmox.objects.filter(Q(id_rfid__icontains=request.POST['busca']), name__isnull=True)
                    else:
                        rows = ItemAmox.objects.filter(Q(id_rfid__icontains=request.POST['busca']))
                else:
                    rows = ItemAmox.objects.filter(Q(name__icontains=request.POST['busca']))
            else:
                rows = ItemAmox.objects.filter()

        dados = {
            'titulo': 'Items - Buscar',
            'rows': rows,
            'fields': fields,
            'cad_pen': cad_pen
        }
        return render(request, 'item/buscar.html', dados)
    else:
        return redirect('/admin/')


def editar(request, id):
    if request.user.is_authenticated:
        item = ItemAmox.objects.filter(id=id).last()
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
            item = ItemAmox.objects.filter(id=request.POST['id']).last()
            if item is not None:
                item.name = request.POST['name']
                item.save()

                messages.success(request, 'Alterações Gravadas com Sucesso!')
                return redirect('buscar_item')
        else:
            return redirect('index')
    else:
        return redirect('index')
