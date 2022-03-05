from django.urls import path

from AmoxProject.views import esp_session, teste

urlpatterns = [
    path('amox/register/item/<str:encode>', esp_session.esp_session, name='amox_register_item'),
    path('amox/login/esp_user/<str:encode>', esp_session.login_esp_user, name='login_esp_user'),
    path('amox/logout/esp_user/<str:encode>', esp_session.logout_esp_user, name='logout_esp_user'),
    path('amox/teste', teste.teste, name='teste')
]
