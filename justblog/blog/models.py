from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return f"{self.author}'s post"


    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})