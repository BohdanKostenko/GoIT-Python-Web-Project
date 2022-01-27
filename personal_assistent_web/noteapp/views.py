from django.shortcuts import render
from django.http import HttpResponse


def noteapp(request):
    return render(request, 'noteapp/noteapp.html')