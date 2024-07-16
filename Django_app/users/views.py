from django.shortcuts import render
from .forms import LoginRegisterForm
from django.contrib.auth.views import LoginView
# Create your views here.

class LoginUser(LoginView):
    form_class = LoginRegisterForm
    template_name = 'users/login_page.html'
    extra_context = {'title': "Login"}
    

def home(request):
    return render(request, 'users/home.html')

def register_page(request):
    form = LoginRegisterForm
    data = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'users/register_page.html', data)
