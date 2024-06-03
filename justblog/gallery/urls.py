from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.GalleryListView.as_view(), name='gallery'),
    path('upload/', views.UploadImageView.as_view(), name='new_image_upload'),
    path('delete/<int:pk>/', views.DeleteImageView.as_view(), name='image_delete'),
]
