from django.shortcuts import render
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import CreateView, TemplateView, ListView
from django.urls import reverse_lazy
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

class home(LoginRequiredMixin,ListView):
    template_name='users/home.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return UserPost.objects.select_related('author').filter(
        author__in=self.request.user.subscriptions.values_list('subscribed_to', flat=True)
        ).order_by('-created_at')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timediff_posts'] = [
            {'post': post, 'time_diff': self.get_time_diff(post.created_at)}
            for post in context['posts']
        ]
        return context

    def get_time_diff(self, created_at):
        time_diff = timezone.now() - created_at
        hours = time_diff.seconds // 3600
        minutes = (time_diff.seconds // 60) % 60
        seconds = time_diff.seconds % 60
        days = hours // 24
        #return f"{hours} hours, {minutes} minutes, {seconds} seconds ago"

        if days > 0:
            if days > 1:
                return f"{days} days ago"
            else:
                return f"{days} day ago"
        elif hours >0:
            if hours > 1:
                return  f"{hours} hours ago"
            else:
                return  f"{hours} hour ago"
        elif minutes > 0:
            if minutes > 1:
                return  f"{minutes} minutes ago"
            else:
                return  f"{minutes} minute ago"
        else:
            if seconds > 1:
                return  f"{seconds} seconds ago"
            else:
                return  f"{seconds} second ago"

