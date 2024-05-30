from django.shortcuts import render
from django.views import generic
from .models import Gallery


class GalleryListView(generic.ListView):
    template_name = 'gallery/gallery.html'
    queryset = Gallery.objects.all()
