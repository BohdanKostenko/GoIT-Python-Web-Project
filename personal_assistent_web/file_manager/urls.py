from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_manager, name='file_manager')
]