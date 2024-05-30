from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_pics')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 400 and img.height > 600:
            output_size = (400, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)
