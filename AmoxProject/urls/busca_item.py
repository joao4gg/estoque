from django.urls import path

from AmoxProject.views import item

urlpatterns = [
    path('amox/busca/item', item.buscar, name='buscar_item'),
]
