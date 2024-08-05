from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView, ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import UserPost


# Create your views here.

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
        user = User.objects.get(username=username)
        return UserPost.objects.filter(author=user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.kwargs['username']
        return context
    

