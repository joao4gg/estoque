from django.db.models import Q
from django.shortcuts import render, redirect
from AmoxProject.models.item_amox import ItemAmox


def buscar(request):
    if request.user.is_authenticated:
        if request.user.has_perm('AmoxProject.view_itemamox'):
            fields = dict()
            if request.method == 'GET':
                rows = ItemAmox.objects.filter()
            else:
                fields = {'busca': request.POST['busca'], 'filtro': request.POST['filtro']}
                if request.POST['busca'] != '':
                    if request.POST['filtro'] == 'id_rfid':
                        rows = ItemAmox.objects.filter(Q(id_rfid__icontains=request.POST['busca']))
                    else:
                        rows = ItemAmox.objects.filter(Q(name__icontains=request.POST['busca']))
                else:
                    rows = ItemAmox.objects.filter()

            dados = {
                'titulo': 'Items - Buscar',
                'rows': rows,
                'fields': fields
            }
            return render(request, 'item/buscar.html', dados)
        else:
            return redirect('/admin/')
    else:
        return redirect('/admin/')
