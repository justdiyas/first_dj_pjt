from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.register, name='user-register'),
    path('login/', views.login.as_view(), name='user-login')
]
