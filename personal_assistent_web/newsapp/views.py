from django.http import HttpResponse
from django.shortcuts import render
from .news import bbc_tech, bbc_sceince, bbc_health, bbc_sport, liga_sport, liga_health, liga_sceince, liga_tech


def newsapp(request):
    return render(request, 'newsapp/newsapp.html')


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
    if not q:
        return HttpResponse('Please submit a search term.')
    else:
        if q == "TECH":
            results = [bbc_tech(), liga_tech()]
        elif q == "SCIENCE":
            results = [bbc_sceince(), liga_sceince()]
        elif q == 'HEALTH':
            results = [bbc_health(), liga_health()]
        elif q == 'SPORT':
            results = [bbc_sport(), liga_sport()]
        else:
            results = [bbc_tech(), bbc_sceince(), bbc_health(), bbc_sport(), liga_sport(), liga_health(),
                       liga_sceince(), liga_tech()]

        return render(request, 'newsapp/search.html', {'results': results, 'query': q})


def search_form(request):
    return render(request, 'newsapp/search_form.html')


def output(request):
    return render(request, 'newsapp/output.html')
