from django.shortcuts import render


def newsapp(request):
    return render(request, 'newsapp/newsapp.html')
