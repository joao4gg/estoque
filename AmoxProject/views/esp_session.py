from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from AmoxProject.master import basic_decode
from AmoxProject.models.item_amox import ItemAmox


@csrf_exempt
def esp_session(request):
    if request.method == 'POST':
        body = basic_decode(request.POST['payload'])

        model = ItemAmox.objects.create()
        model.id_rfid = body['id']
        model.sac = body['sac']
        model.picc = body['picc']
        model.save()

    else:
        return HttpResponse(403)
