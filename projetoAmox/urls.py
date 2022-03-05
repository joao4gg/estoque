from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from AmoxProject import views
from projetoAmox import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('AmoxProject.urls.esp_session')),
    path('', include('AmoxProject.urls.busca_item')),
    path('', include('AmoxProject.urls.user')),
    path('', include('AmoxProject.urls.relatorios')),
    path('menu/notification', views.search_menu_notification, name='search_menu_notification'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
