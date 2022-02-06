from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.file_manager, name='file_manager'),
    path('file_manager', views.my_view, name='file_manager'),
    path('file_manager_choice/', views.choice, name='file_manager_choice'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)