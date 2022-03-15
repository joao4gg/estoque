from django.contrib.auth.models import User
from django.db import models

from AmoxProject.models.item_estoque import ItemEstoque


class ItemAux(models.Model):
    id_item = models.ForeignKey(ItemEstoque, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    data = models.DateTimeField(null=True, default=None)

