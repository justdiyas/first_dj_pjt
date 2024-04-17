from django.shortcuts import render
from django.views import generic
from .models import Post


class mainListView(generic.ListView):
    template_name = 'blog/base_blog.html'
    queryset = Post.objects.all()


def home(request):
    return render(request, 'blog/home.html')


