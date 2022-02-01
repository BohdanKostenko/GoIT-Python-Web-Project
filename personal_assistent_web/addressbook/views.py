from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm
from django.db.models import Q, CharField
from django.db.models.functions import Lower


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


def edit(request, contact_id):
    edit_contact = get_object_or_404(Contact, pk=contact_id)

    if request.method == "POST":
        edit_contact.name = request.POST.get("name")
        edit_contact.phone = request.POST.get("phone")
        edit_contact.birthday = request.POST.get("birthday")
        edit_contact.email = request.POST.get("email")
        edit_contact.address = request.POST.get("address")
        edit_contact.save()
        return render(request, 'addressbook/detail.html', {'contact': edit_contact})

    return render(request, 'addressbook/edit.html', {'contact': edit_contact})


def search(request):
    CharField.register_lookup(Lower, "lower")
    if 'q' in request.GET:
        q = request.GET['q']
    if not q:
        return HttpResponse('Please submit a search term.')
    else:
        contacts = Contact.objects.filter(Q(name__iregex=q))
        return render(request, 'addressbook/search.html', {'contacts': contacts, 'query': q})


def search_form(request):
    return render(request, 'addressbook/search_form.html')
