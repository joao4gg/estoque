from django.urls import path

from AmoxProject.views import user

urlpatterns = [
    path('amox/user/buscar', user.buscar, name='user_buscar'),
    path('amox/user/inserir', user.inserir, name='user_inserir'),
    path('amox/user/atualizar', user.atualizar, name='user_atualizar'),
    path('amox/user/editar/<int:id>', user.editar, name='user_editar'),
]
