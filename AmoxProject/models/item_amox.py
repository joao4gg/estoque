from django.db import models


class ItemAmox(models.Model):
    id_rfid = models.CharField(max_length=128, null=True, default=None)
    sac = models.CharField(max_length=128, null=True, default=None)
    picc = models.CharField(max_length=128, null=True, default=None)

