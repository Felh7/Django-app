from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
# Create your views here.

class post_page(FormView):
    form_class = UploadFileForm
    template_name='posts/posts.html'
    checked = True


