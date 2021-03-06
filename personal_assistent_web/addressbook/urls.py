from django.urls import path
from . import views

urlpatterns = [
    path('', views.addressbook, name='addressbook'),
    path('addressbook', views.addressbook, name='addressbook'),
    path('addressbook_create', views.create, name='addressbook_create'),
    path('addressbook_show', views.show, name='addressbook_show'),
    # ex: /addressbook/addressbook_contact/5/
    path('addressbook_contact/<int:contact_id>/', views.detail, name='detail'),
    # ex: /addressbook/addressbook_contact/5/edit/
    path('addressbook_contact/<int:contact_id>/edit', views.edit, name='edit'),
    # ex: /addressbook/addressbook_contact/5/delete/
    path('addressbook_contact/<int:contact_id>/delete', views.delete, name='delete'),
    path('addressbook_search/', views.search, name='addressbook_search'),
    path('addressbook_search_form/', views.search_form, name='addressbook_search_form'),
    path('addressbook_input_form/', views.birthday_form, name='addressbook_input_form'),
    path('addressbook_birthday/', views.birthday, name='addressbook_birthday'),
]
