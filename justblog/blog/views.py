from django.views import generic
from .models import Post
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404


class HomeView(TemplateView):
    model = User
    template_name = 'blog/home.html'


class PostListView(generic.ListView):
    template_name = 'blog/blog.html'
    queryset = Post.objects.all()
    ordering = ['-publication_date']
    paginate_by = 5


class UserPostListView(generic.ListView):
    model = Post
    template_name = 'blog/user_blog.html'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-publication_date')

class PostDetailView(generic.DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Post
    fields = ['title', 'content']
    success_message = 'New blog post has been created!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'content']
    success_message = 'Blog post has been updated!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.DeleteView):
    model = Post
    success_url = '/home/blog/'
    success_message = 'Blog post has been deleted!'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False