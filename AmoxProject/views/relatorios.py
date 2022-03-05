import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template
import pandas as pd

from AmoxProject.models.item_amox import ItemAmox


def rel_itens(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            itens = ItemAmox.objects.filter()

            dados = {
                'rows': itens,
            }

            template = get_template('relatorios/relatorio_itens.html')
            dados = template.render(dados)

            dados = pd.read_html(dados)[0]
            name = 'media/planilhas/rel_itens' + str(datetime.now().timestamp()).replace('.', '') + '.xlsx'
            dados.to_excel(name, index=False)
            return HttpResponse(json.dumps({'path': f'/{name}'}))

    else:
        return redirect('index')
