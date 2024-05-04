from django.views import generic
from .models import Post
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render


class HomeView(TemplateView):
    model = User
    template_name = 'blog/home.html'


class PostListView(generic.ListView):
    template_name = 'blog/blog.html'
    queryset = Post.objects.all()
    ordering = ['-publication_date']


class PostDetailView(generic.DetailView):
    model = Post
