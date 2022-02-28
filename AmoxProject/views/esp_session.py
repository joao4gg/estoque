from datetime import datetime

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from AmoxProject.master import basic_decode
from AmoxProject.models.item_amox import ItemAmox


@csrf_exempt
def esp_session(request, encode):
    if request.method == 'POST':
        body = basic_decode(encode)

        item = ItemAmox.objects.filter(id_rfid=body['id']).last()
        if item is not None:
            if item.available:
                item.available = False
            else:
                item.available = True

        else:
            model = ItemAmox.objects.create()
            model.id_rfid = body['id']
            model.data_last_alt = datetime.now()
            model.save()

        return HttpResponse(200)
    else:
        return HttpResponse(403)
