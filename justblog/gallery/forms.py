from django.forms import ModelForm
from .models import Gallery


class UploadImageForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image']


class UpdateImageForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['title']
