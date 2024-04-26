from django.views import generic
from .models import Post
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render

class MainListView(generic.ListView):
    template_name = 'blog/blog.html'
    queryset = Post.objects.all()


class HomeView(TemplateView):
    model = User
    template_name = 'blog/home.html'

