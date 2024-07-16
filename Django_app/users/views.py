from django.shortcuts import render
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login_page.html'
    extra_context = {'title': "Login"}
    
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register_page.html'
    extra_context = {'title': "Register"}
    success_url = reverse_lazy('users:login')

def home(request):
    return render(request, 'users/home.html')