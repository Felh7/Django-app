from django.shortcuts import render
from .forms import LoginRegisterForm
# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def login_page(request):
    form = LoginRegisterForm
    data = {
        'title': 'Login',
        'form': form,
    }
    return render(request, 'users/login_page.html', data)

def register_page(request):
    form = LoginRegisterForm
    data = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'users/register_page.html', data)
