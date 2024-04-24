from django.shortcuts import render
from .models import Question
from django.views import generic

class IndexListView(generic.ListView):
    template_name = 'polls/index.html'
    queryset = Question.objects.all()


