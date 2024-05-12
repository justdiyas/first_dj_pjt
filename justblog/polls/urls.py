from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexListView.as_view(), name='polls-index'),
    path('user/<str:username>/', views.UserPollListView.as_view(), name='user-polls'),
    path('<int:pk>/detail/', views.IndexDetailView.as_view(), name='polls-detail'),
    path('<int:pk>/vote/', views.vote, name='polls-vote'),
    path('<int:pk>/vote/result/', views.ResultDetailView.as_view(), name='polls-result'),
    path('new/', views.PollCreateView.as_view(), name='polls-create'),
    path('new/<int:pk>/choice/', views.create_choice, name='choice-create'),
    path('<int:pk>/choice/update/', views.update_choice, name='choice-update'),
    path('<int:pk>/delete/', views.PollDeleteView.as_view(), name='polls-delete'),
]