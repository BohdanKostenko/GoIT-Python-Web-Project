from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsapp, name='newsapp'),
    path('newsapp', views.newsapp, name='newsapp'),
    path('newsapp_search/', views.search, name='newsapp_search'),
    path('newsapp_search_form/', views.search_form, name='newsapp_search_form'),
]
