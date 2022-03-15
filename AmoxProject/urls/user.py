from django.urls import path

from AmoxProject.views import user

urlpatterns = [
    path('login', user.login, name='user_login'),
    path('logout', user.logout, name='user_logout'),
    path('estoque/user/buscar', user.buscar, name='user_buscar'),
    path('estoque/user/inserir', user.inserir, name='user_inserir'),
    path('estoque/user/atualizar', user.atualizar, name='user_atualizar'),
    path('estoque/user/editar/<int:id>', user.editar, name='user_editar'),
]
