from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *
from .forms import NotesForm, CategoryForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.db.models import Q, CharField
from django.db.models.functions import Lower
from django.urls import reverse_lazy


def choice(request):
    CharField.register_lookup(Lower, "lower")
    if 'q' in request.GET:
        q = request.GET['q']
    if not q:
        return HttpResponse('Please submit a search term.')
    else:
        if q == "education":
            tags = Notes.objects.filter(tag__name='education')
        elif q == "annotation":
            tags = Notes.objects.filter(Q(tag__name='annotation'))
        elif q == 'chronicle':
            tags = Notes.objects.filter(Q(tag__name="chronicle"))
        elif q == 'opened information':
            tags = Notes.objects.filter(Q(tag__name='opened information'))
        elif q == 'announcement':
            tags = Notes.objects.filter(Q(tag__name="announcement"))
        elif q == 'private note':
            tags = Notes.objects.filter(Q(tag__name="private note"))
        elif q == 'event note':
            tags = Notes.objects.filter(Q(tag__name="event note"))
        elif q == 'business note':
            tags = Notes.objects.filter(Q(tag__name="business note"))
        elif q == 'review':
            tags = Notes.objects.filter(Q(tag__name="review"))
        elif q == 'mini story':
            tags = Notes.objects.filter(Q(tag__name="mini story"))
        else:
            tags = Notes.objects.all()

        return render(request, 'noteapp/choice_page.html', {'tags': tags, 'query': q})


def noteapp(request):
    notes = Notes.objects.order_by('-pub_date')
    return render(request, 'noteapp/noteapp.html', {'title': 'Noteapp page', 'notes': notes})


class NoteCreateView(CreateView):
    model = Notes
    template_name = 'noteapp/create_note.html'
    form_class = NotesForm
    success_url = reverse_lazy('noteapp')


class NoteDetailView(DetailView):
    model = Notes
    template_name = 'noteapp/details_views.html'
    context_object_name = 'article'


# def update(request, note_id):
#     update_note = Notes.objects.get(note_id)
#
#     if request.method == "POST":
#         update_note.tag = request.POST.get("tag")
#         update_note.note = request.POST.get("note")
#         update_note.save()
#         return render(request, 'noteapp/details_views.html', {'note': update_note})
#
#     return render(request, "{% url 'note-update' %}", {'note': update_note})

class NoteUpdateView(UpdateView):
    model = Notes
    template_name = 'noteapp/create_note.html'
    form_class = NotesForm


class NoteDeleteView(DeleteView):
    model = Notes
    success_url = reverse_lazy('noteapp')
    template_name = 'noteapp/delete_note.html'


def search_views(request):
    CharField.register_lookup(Lower, "lower")
    if 'q' in request.GET:
        q = request.GET['q']
    if not q:
        return HttpResponse('Please submit a search term.')
    else:
        notes = Notes.objects.filter(Q(note__iregex=q))
        return render(request, 'noteapp/search_results.html', {'notes': notes, 'query': q})


def search_form(request):
    return render(request, 'noteapp/search_form.html')


def create_note(request):
    error = ''
    if request.method == 'POST':
        data_request = request.POST
        form = NotesForm(data_request)
        if form.is_valid():
            form.save()
            return redirect('noteapp')
        else:
            error = 'Invalid form'

    form = NotesForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'noteapp/create_note.html', context)


def dropdown_menu(request):
    form = CategoryForm
    context = {
        'form': form,
           }
    return render(request, 'noteapp/create_note.html', context)
