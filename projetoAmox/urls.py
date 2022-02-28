from django.contrib import admin
from django.urls import path, include

from AmoxProject import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('AmoxProject.urls.esp_session')),
    path('', include('AmoxProject.urls.busca_item'))

]
