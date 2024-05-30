from django.shortcuts import render, redirect
from django.views import generic
from .models import Gallery
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UploadImageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class GalleryListView(generic.ListView):
    template_name = 'gallery/gallery.html'
    queryset = Gallery.objects.all()
    paginate_by = 10


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
