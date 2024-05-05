from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexListView.as_view(), name='polls-index'),
    path('<int:pk>/detail/', views.IndexDetailView.as_view(), name='polls-detail'),
    path('<int:pk>/vote/', views.vote, name='polls-vote'),
    path('<int:pk>/vote/result/', views.ResultDetailView.as_view(), name='polls-result'),
    path('new/', views.QuestionCreateView.as_view(), name='create-question'),
]