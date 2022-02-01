from django.urls import path
from . import views

urlpatterns = [
    path('', views.addressbook, name='addressbook'),
    path('addressbook', views.addressbook, name='addressbook'),
    # ex: /addressbook/addressbook_create
    path('addressbook_create', views.create, name='addressbook_create'),
    # ex: /addressbook/addressbook_show
    path('addressbook_show', views.show, name='addressbook_show'),
    # ex: /addressbook/addressbook_contact/5/
    path('addressbook_contact/<int:contact_id>/', views.detail, name='detail'),
    # ex: /addressbook/addressbook_contact/5/edit/
    path('addressbook_contact/<int:contact_id>/edit', views.edit, name='edit'),
    # ex: /addressbook/addressbook_contact/5/delete/
    path('addressbook_contact/<int:contact_id>/delete', views.delete, name='delete'),
    # # ex: /addressbook/search/
    path('search/', views.search, name='search'),
    path('search_form/', views.search_form, name='search_form'),
    # ex: /addressbook/search_results/
    # path('search_results', views.search, name='search'),
]