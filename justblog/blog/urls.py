from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.HomeView.as_view(), name='blog-home'),
    path('blog/', views.PostListView.as_view(), name='blog-main'),
    path('blog/post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]