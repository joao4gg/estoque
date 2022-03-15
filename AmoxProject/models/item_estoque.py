from django.contrib.auth.models import User
from django.db import models

from AmoxProject.models.tipo_und import TipoUnd


class ItemEstoque(models.Model):
    name = models.CharField(max_length=256, null=True, default=None)
    codigo = models.CharField(max_length=128, null=True, default=None)
    id_und = models.ForeignKey(TipoUnd, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    qtde = models.IntegerField(default=0)


