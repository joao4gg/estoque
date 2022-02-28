from django.http import HttpResponse
from django.shortcuts import render

from AmoxProject.master import basic_decode
from AmoxProject.models.item_amox import ItemAmox


def buscar(request):
    if request.method == 'GET':
        rows = ItemAmox.objects.filter()
        dados = {
            'rows': rows
        }

        return render(request, 'item/buscar.html', dados)
    else:
        return HttpResponse(403)
