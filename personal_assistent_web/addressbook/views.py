from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm


def addressbook(request):
    return render(request, 'addressbook/addressbook.html')


def show(request):
    latest_contact_list = Contact.objects.order_by('name')
    context = {'latest_contact_list': latest_contact_list}
    return render(request, 'addressbook/contacts.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addressbook')
        else:
            error = "Форма была неверной"
    form = ContactForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'addressbook/addressbook_create.html', context)


def detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'addressbook/detail.html', {'contact': contact})


def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id).delete()
    return render(request, 'addressbook/delete.html', {'contact': contact})

def edit(request):
    return render(request, 'addressbook/addressbook.html')