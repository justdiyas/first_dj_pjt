from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('blog/', views.MainListView.as_view(), name='blog-main'),
    path('', views.HomeView.as_view(), name='blog-home'),
]