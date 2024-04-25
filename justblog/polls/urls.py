from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexListView.as_view(), name='polls-index'),
    path('<int:pk>/detail/', views.IndexDetailView.as_view(), name='polls-detail'),
    path('<int:pk>/vote/', views.vote, name='polls-vote'),
]