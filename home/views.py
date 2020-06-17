from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator

# Create your views here.

class BlogPageView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 3 # 2post gorsenecek

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post.html'
