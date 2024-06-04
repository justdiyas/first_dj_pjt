from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Gallery
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from .forms import UploadImageForm, UpdateImageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class GalleryListView(generic.ListView):
    template_name = 'gallery/gallery.html'
    queryset = Gallery.objects.all()
    paginate_by = 16


# @login_required
# def upload_image(request):
#     if request.method == 'POST':
#         form = UploadImageForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'New image has been succesfully uploaded!')
#             return redirect('gallery:gallery')
#     else:
#         form = UploadImageForm(instance=request.user)
#     return render(request, 'gallery/upload_image.html', {'form': form})

class UploadImageView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Gallery
    form_class = UploadImageForm
    template_name = 'gallery/upload_image.html'
    success_message = 'New image has been successfully uploaded!'
    success_url = '/gallery/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateImageView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Gallery
    form_class = UpdateImageForm
    template_name = 'gallery/update_image.html'
    success_message = 'Gallery photo has been updated!'
    success_url = '/gallery/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.user:
            return True
        return False


class DeleteImageView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.DeleteView):
    model = Gallery
    template_name = 'gallery/delete_image.html'
    success_url = '/gallery/'
    success_message = 'Photo has been deleted!'

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.user:
            return True
        return False


class UserGalleryView(generic.ListView):
    model = Gallery
    template_name = 'gallery/user_gallery.html'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Gallery.objects.filter(user=user)
