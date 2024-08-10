from django.shortcuts import render
from .forms import LoginUserForm, RegisterUserForm, ResetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.views.generic import CreateView, TemplateView, ListView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import UserSubscriptions, UserPost
from django.utils import timezone



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

class PasswordReset(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'users/reset_password_page.html'
    extra_context = {'title': "Reset Password"}
    success_url = reverse_lazy('users:password-reset-done')
    html_email_template_name = 'users/reset_password_email.html'
    email_template_name = 'users/reset_password_email.html'

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'users/reset_password_confirm.html'
                                              

