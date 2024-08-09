from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView, ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import PostCreateForm
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import UserPost, UserFollowers, UserSubscriptions
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def checksubscription_ajax(request):
    if request.method == 'POST' and request.user.is_authenticated:
        author_username = request.POST.get('author')
        try:
            author = User.objects.get(username=author_username)
            subscribed = UserSubscriptions.objects.filter(user=request.user, subscribed_to=author).exists()
            return JsonResponse({'subscribed': subscribed})
        except ObjectDoesNotExist:
            return JsonResponse({'subscribed': False})
    else:
        return JsonResponse({'subscribed': False})
    
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

def unsubscribe_ajax(request):
    if request.method == 'POST':
        author_username = request.POST.get('author')
        try:
            author = User.objects.get(username=author_username)
            UserSubscriptions.objects.filter(user=request.user, subscribed_to=author).delete()
            UserFollowers.objects.filter(follower=request.user, user=author).delete()

            return JsonResponse({'subscribed': False})
        except ObjectDoesNotExist:
            return JsonResponse({'subscribed': True, 'error': 'Author not found'})
    else:
        return JsonResponse({'subscribed': True})

def CheckIfLiked_ajax(request):
    if request.method == 'GET' and request.user.is_authenticated:
        post_id = request.GET.get('post_id')
        try:
            userpost = UserPost.objects.get(id=post_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
        if userpost.liked_by.filter(id=request.user.id).exists():
            return JsonResponse({'liked': True})
        else:
            return JsonResponse({'liked': False})
    else:
        return JsonResponse({'error': 'You must be logged in to like a post'}, status=401)
    
def likePost_ajax(request):
    if request.method == 'POST' and request.user.is_authenticated:
        post_id = request.POST.get('post_id')
        try:
            userpost = UserPost.objects.get(id=post_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
        userpost.liked_by.add(request.user)
        return JsonResponse({'liked': True})
    else:
        return JsonResponse({'error': 'You must be logged in to like a post'}, status=401)

def unlikePost_ajax(request):
    if request.method == 'POST' and request.user.is_authenticated:
        post_id = request.POST.get('post_id')
        try:
            userpost = UserPost.objects.get(id=post_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
        userpost.liked_by.remove(request.user)
        return JsonResponse({'liked': False})
    else:
         return JsonResponse({'error': 'You must be logged in to like a post'}, status=401)

class post_page(FormView):
    form_class = PostCreateForm
    template_name='posts/add_post.html'
    success_url = reverse_lazy('posts:add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

class profile_page(ListView):
    model = UserPost
    template_name='posts/profile.html'
    context_object_name = 'posts'

    def get(self, request, *args, **kwargs):
        username = self.kwargs['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # If the user does not exist, raise a 404 error
            raise Http404("User not found")
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        username = self.kwargs['username']
        return UserPost.objects.select_related('author').filter(author__username=username).order_by('-created_at')
    
    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return "posts.html"
        else:
            return self.template_name
        
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
        days = time_diff.days
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

       


