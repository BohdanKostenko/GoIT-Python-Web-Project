from django.urls import path
from . import views

urlpatterns = [
    path('', views.noteapp, name='noteapp'),
    path('create_note', views.NoteCreateView.as_view(), name='create-note'),
    path('<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
    path('<int:pk>/update', views.NoteUpdateView.as_view(), name='note-update'),
    path('<int:pk>/delete', views.NoteDeleteView.as_view(), name='note-delete'),
    path('noteapp/search_results', views.search_views, name='search_views'),
    path('noteapp/search_form', views.search_form, name='search_form'),
    path('noteapp/choice_page', views.choice, name='choice_page'),
]

# path('create_note', views.create_note, name='create_note'),