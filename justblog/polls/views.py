from .models import Question
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class IndexListView(generic.ListView):
    template_name = 'polls/polls_index.html'
    queryset = Question.objects.all()


class IndexDetailView(generic.DetailView):
    model = Question
    template_name = 'polls/polls_detail.html'

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    messages.success(request, f'Your vote is counted')
    return HttpResponseRedirect(reverse('polls:polls-detail', args=(question.id,)))