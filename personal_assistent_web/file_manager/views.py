from django.shortcuts import render


def file_manager(request):
    return render(request, 'file_manager/file_manager.html')