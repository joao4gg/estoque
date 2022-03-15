from django.urls import path

from AmoxProject.views import item

urlpatterns = [
    path('estoque/busca/item', item.buscar, name='buscar_item'),
    path('estoque/item/editar/<int:id>', item.editar, name='editar_item'),
    path('estoque/item/atualizar', item.atualizar, name='atualizar_item'),
    path('estoque/item/inserir', item.inserir, name='inserir_item')
]
