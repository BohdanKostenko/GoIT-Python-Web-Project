from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'


def signup(request):
    return render(request, 'main/signup.html')


def index(request):
    return render(request, 'main/index.html')
