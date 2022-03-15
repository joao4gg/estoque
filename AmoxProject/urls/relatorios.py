from django.urls import path

from AmoxProject.views import relatorios

urlpatterns = [
    path('estoque/relatorio/itens', relatorios.rel_itens, name='estoque_rel_itens'),
]
