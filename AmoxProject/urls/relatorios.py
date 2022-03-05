from django.urls import path

from AmoxProject.views import relatorios

urlpatterns = [
    path('amox/relatorio/itens', relatorios.rel_itens, name='amox_rel_itens'),
]
