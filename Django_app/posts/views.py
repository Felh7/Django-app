from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


# Create your views here.

class post_page(FormView):
    form_class = UploadFileForm
    template_name='posts/posts.html'
    checked = True
    success_url = reverse_lazy('posts:posts')
    def form_valid(self, form):
        username = self.request.user.username
        form.instance.username = username
        form.save()
        return super().form_valid(form)

class profile_page(DetailView):
    model = User
    template_name='posts/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    

