from django.contrib.auth.models import User
from django.db import models


class AuxUser(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    code_pass = models.CharField(max_length=256, null=True, default=None)
    last_login = models.DateTimeField(null=True, default=None)
    logout_dt = models.DateTimeField(null=True, default=None)
