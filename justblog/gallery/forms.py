from django.forms import ModelForm
from .models import Gallery, Description

# ImageFormSet = inlineformset_factory(Gallery, Description, fields=['text'], extra=1, can_delete=False)
# UpdateFormSet = inlineformset_factory(Gallery, Description, fields=['text'])


class UploadImageForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image']


class UpdateImageForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['title']


# class DescriptionForm(ModelForm):
#     class Meta:
#         model = Description
#         fields = ['text']
