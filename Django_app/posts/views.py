from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView, ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import UploadFileForm
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import UserPost, UserFollowers, UserSubscriptions
from django.utils import timezone
from datetime import datetime


# Create your views here.
def subscribe_ajax(request):
    if request.method == 'POST':
        author_username = request.POST.get('author')
        author = User.objects.get(username=author_username)

        subscribed, created = UserSubscriptions.objects.get_or_create(user=request.user, subscribed_to=author)
        if created:
            UserFollowers.objects.get_or_create(follower=request.user, user=author)
            return JsonResponse({'subscribed': True})
        else:
          return JsonResponse({'subscribed': False})
    else:
        return Http404

class post_page(FormView):
    form_class = UploadFileForm
    template_name='posts/posts.html'
    success_url = reverse_lazy('posts:posts')
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

class profile_page(ListView):
    model = UserPost
    template_name='posts/profile.html'
    context_object_name = 'posts'
    def get_queryset(self):
        username = self.kwargs['username']
        return UserPost.objects.select_related('author').filter(author__username=username).order_by('-created_at')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.kwargs['username']
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

       


