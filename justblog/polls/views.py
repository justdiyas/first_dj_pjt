from .models import Question, Choice
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.contrib import messages

class IndexListView(generic.ListView):
    template_name = 'polls/polls_index.html'
    queryset = Question.objects.all()


class IndexDetailView(generic.DetailView):
    model = Question
    template_name = 'polls/polls_detail.html'


class ResultDetailView(generic.DetailView):
    model = Question
    template_name = 'polls/polls_result.html'


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        messages.warning(request, 'You have not picked a choice. Try again!')
        return render(request, 'polls/polls_detail.html', {'question': question})
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        messages.success(request, 'Your voice is counted')
        return HttpResponseRedirect(reverse('polls:polls-result', args=(question.id,)))