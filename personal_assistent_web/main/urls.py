from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('about', views.about, name='about')
]