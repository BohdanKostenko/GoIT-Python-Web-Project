from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm
from django.db.models import Q, CharField
from django.db.models.functions import Lower
from datetime import datetime, timedelta


def addressbook(request):
    return render(request, 'addressbook/addressbook.html')


def show(request):
    user_id = request.user.id
    # latest_contact_list = Contact.objects.order_by('name')
    latest_contact_list = Contact.objects.filter(user_id=user_id).order_by('name')
    context = {'latest_contact_list': latest_contact_list}
    return render(request, 'addressbook/contacts.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        data_request = request.POST
        user_id = request.user.id
        form = ContactForm(data_request)
        if form.is_valid():
            # form.save()
            Contact.objects.create(
                name=data_request['name'],
                phone=data_request['phone'],
                birthday=data_request['birthday'],
                email=data_request['email'],
                address=data_request['address'],
                user_id=user_id
            )
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
    user_id = request.user.id
    if 'q' in request.GET:
        q = request.GET['q']
    if not q:
        return HttpResponse('Please submit a search term.')
    else:
        contacts = Contact.objects.filter(user_id=user_id).filter(Q(name__iregex=q))
        return render(request, 'addressbook/search.html', {'contacts': contacts, 'query': q})


def search_form(request):
    return render(request, 'addressbook/search_form.html')


def birthday_form(request):
    user_id = request.user.id
    now = datetime.today()
    contacts = Contact.objects.filter(user_id=user_id).filter(birthday__month=now.strftime("%m"))
    next_contacts = Contact.objects.filter(user_id=user_id).filter(birthday__month=(now.month + 1))
    return render(request, 'addressbook/input_form.html', {'contacts': contacts, 'next_contacts': next_contacts})


def birthday(request):
    user_id = request.user.id
    now = datetime.today()
    if 'q' in request.GET:
        q = request.GET['q']
    if not q:
        return HttpResponse('Please submit a search term.')
    else:
        # contacts = Contact.objects.filter(
        #     Q(birthday__month__lte=(now + timedelta(int(q))).strftime("%m")),
        #     Q(birthday__month__gte=now.strftime("%m")))
        contacts = Contact.objects.filter(user_id=user_id).raw(
            f'SELECT * FROM addressbook_contact WHERE dayofyear(birthday) between dayofyear(now()) and dayofyear(now() + interval {q} day)')

    return render(request, 'addressbook/birthday.html',
                  {'contacts': contacts, 'query': q, 'data': (now + timedelta(int(q))).strftime("%m-%d-%Y")})
