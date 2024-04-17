from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('blog/', views.mainListView.as_view(), name='blog-main'),
    path('', views.home, name='blog-home'),
]