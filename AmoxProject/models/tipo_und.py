from django.db import models


class TipoUnd(models.Model):
    nome = models.CharField(max_length=256, null=True, default=None)


