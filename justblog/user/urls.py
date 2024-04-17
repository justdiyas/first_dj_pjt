from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.register, name='user-register'),
    path('login/', views.LoginView.as_view(), name='user-login'),
    path('logout/', views.logout_view, name='user-logout'),
    path('profile/', views.profile, name='user-profile'),
]
