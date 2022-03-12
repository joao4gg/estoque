import datetime
from datetime import timedelta

from django.contrib.auth.models import User

from AmoxProject.models.aux_user import AuxUser


def get_user_session():
    users = AuxUser.objects.filter(logout_dt__isnull=True).order_by('last_login')
    sub_date = (datetime.datetime.now() - timedelta(hours=1))
    retorno = None
    for user in users:
        if user.last_login is not None:
            if user.last_login > sub_date:
                retorno = user
                break

    return retorno

