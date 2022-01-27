from django.shortcuts import render


def addressbook(request):
    return render(request, 'addressbook/addressbook.html')
