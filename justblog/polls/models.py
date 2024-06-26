from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    publication_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def was_published_recently(self):
        week_ago = self.publication_date - datetime.timedelta(days=7)
        return week_ago < self.publication_date < timezone.now()

    def __repr__(self):
        return f'Author: {self.author} \nQuestion: {self.question_text}'

    def get_absolute_url(self):
        return reverse('polls:choice-create', kwargs={'pk': self.pk})

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __repr__(self):
        return self.choice_text

    def get_absolute_url(self):
        return reverse('polls:polls-index', kwargs={'pk': self.pk})