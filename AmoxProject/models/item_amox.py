from django.contrib.auth.models import User
from django.db import models


class ItemAmox(models.Model):
    id_rfid = models.CharField(max_length=128, null=True, default=None)
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    data_last_alt = models.DateTimeField(null=True, default=None)
    available = models.BooleanField(default=True)
    name = models.CharField(max_length=256, null=True, default=None)


