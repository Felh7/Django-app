from django.shortcuts import render
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import CreateView, TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import UserSubscriptions, UserPost


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

class home(LoginRequiredMixin,ListView):
    template_name='users/home.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return UserPost.objects.select_related('author').filter(
        author__in=self.request.user.subscriptions.values_list('subscribed_to', flat=True)
        )


