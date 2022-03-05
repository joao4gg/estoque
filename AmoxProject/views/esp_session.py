from datetime import datetime, timedelta

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from AmoxProject.functions.esp_session import get_user_session
from AmoxProject.master import basic_decode
from AmoxProject.models.aux_user import AuxUser
from AmoxProject.models.item_amox import ItemAmox


@csrf_exempt
def esp_session(request, encode):
    if request.method == 'POST':
        body = basic_decode(encode)

        item = ItemAmox.objects.filter(id_rfid=body['id']).last()
        if item is not None:
            if item.available:
                item.data_last_alt = datetime.now()
                item.available = False
            else:
                item.data_last_alt = datetime.now()
                item.available = True

        else:
            user = get_user_session()

            model = ItemAmox.objects.create()
            model.id_rfid = body['id'].upper()
            model.data_last_alt = datetime.now()
            if user is not None:
                model.id_user = user.id_user
            model.save()

        return HttpResponse(200)
    else:
        return HttpResponse(403)


@csrf_exempt
def login_esp_user(request, encode):
    if request.method == 'POST':
        body = basic_decode(encode)
        user = User.objects.filter(last_name=body['id'].upper()).last()
        if user is not None:
            aux_user = AuxUser.objects.filter(id_user=user).last()
            if aux_user.last_login < datetime.now() - timedelta(hours=1):
                aux_user.last_login = datetime.now()
                user.last_login = datetime.now()
                aux_user.logout_dt = None
                aux_user.save()
                user.save()
                return HttpResponse(f'{user.first_name.split(" ")[0]}', status=200)
            elif aux_user.logout_dt is not None:
                aux_user.last_login = datetime.now()
                user.last_login = datetime.now()
                aux_user.logout_dt = None
                aux_user.save()
                user.save()
                return HttpResponse(f'{user.first_name.split(" ")[0]}', status=200)
            else:
                return HttpResponse('Sessão já Iniciada!', status=202)
        else:
            return HttpResponse('Usuario não Encontrado', status=403)

    else:
        return HttpResponse(403)


@csrf_exempt
def logout_esp_user(request, encode):
    if request.method == 'POST':
        body = basic_decode(encode)
        user = User.objects.filter(last_name=body['id']).last()
        if user is not None:
            aux_user = AuxUser.objects.filter(id_user=user).last()
            if aux_user is not None:
                if aux_user.last_login < datetime.now() - timedelta(hours=2):
                    return HttpResponse(f'Sessão Invalida!', status=402)
                else:
                    aux_user.logout_dt = datetime.now()
                    return HttpResponse(f'{user.first_name.split(" ")[0]}', status=200)

        else:
            return HttpResponse('Usuario não Encontrado', status=403)

    else:
        return HttpResponse(403)
