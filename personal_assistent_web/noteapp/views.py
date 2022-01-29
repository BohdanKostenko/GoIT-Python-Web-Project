from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm


def noteapp(request):
    notes = Notes.objects.all()
    return render(request, 'noteapp/noteapp.html', {'title': 'Noteapp page', 'notes': notes})


def create_note(request):
    error = ''
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Invalid form'

    form = NotesForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'noteapp/create_note.html', context)