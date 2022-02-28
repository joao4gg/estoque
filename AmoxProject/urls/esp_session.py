from django.urls import path

from AmoxProject.views import esp_session

urlpatterns = [
    path('amox/register/item/<str:encode>', esp_session.esp_session, name='amox_register_item'),
]
