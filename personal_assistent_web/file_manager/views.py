from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
from django.http import HttpResponse
from django.db.models import Q, CharField
from django.db.models.functions import Lower


def file_manager(request):
    return render(request, 'file_manager/file_manager.html')


def my_view(request):
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('file_manager')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Render list page with the documents and the form
    context = {'form': form, 'message': message}
    return render(request, 'file_manager/file_manager.html', context)


def choice(request):
    CharField.register_lookup(Lower, "lower")
    if 'q' in request.GET:
        q = request.GET['q']
    if not q:
        return HttpResponse('Please submit a search term.')
    else:
        if q == "VIDEO":
            documents = Document.objects.filter(
                Q(docfile__iregex='.AVI') | Q(docfile__iregex='.MP4') | Q(docfile__iregex='.MOV') | Q(docfile__iregex='.MKV'))
        elif q == "MUSIC":
            documents = Document.objects.filter(
                Q(docfile__iregex='.MP3') | Q(docfile__iregex='.OGG') | Q(docfile__iregex='.WAV') | Q(docfile__iregex='.AMR'))
        elif q == 'IMAGES':
            documents = Document.objects.filter(
                Q(docfile__iregex=".JPEG") | Q(docfile__iregex=".JPG") | Q(docfile__iregex=".PNG") | Q(docfile__iregex=".SVG"))
        elif q == 'DOCUMENTS':
            documents = Document.objects.filter(
                Q(docfile__iregex='.DOC') | Q(docfile__iregex='.DOCX') | Q(docfile__iregex='.TXT') | Q(docfile__iregex='.PDF')| Q(docfile__iregex='.XLSX')| Q(docfile__iregex='.PPTX'))
        elif q == 'ARCH':
            documents = Document.objects.filter(Q(docfile__iregex=".ZIP"))

        else:
            documents = Document.objects.all()

        return render(request, 'file_manager/choice.html', {'documents': documents, 'query': q})


# def choice_form(request):
#     return render(request, 'file_manager/choice_form.html')
