from django.urls import path

from AmoxProject.views import item

urlpatterns = [
    path('amox/busca/item', item.buscar, name='buscar_item'),
    path('amox/item/editar/<int:id>', item.editar, name='editar_item'),
    path('amox/item/atualizar', item.atualizar, name='atualizar_item'),
]
