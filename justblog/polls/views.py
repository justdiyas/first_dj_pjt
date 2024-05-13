from .models import Question, Choice
from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .forms import ChoiceFormSet, ChoiceUpdateFormSet


class IndexListView(generic.ListView):
    template_name = 'polls/polls_index.html'
    queryset = Question.objects.all()
    ordering = ['-publication_date']
    paginate_by = 5


class UserPollListView(generic.ListView):
    template_name = 'polls/user_polls.html'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Question.objects.filter(author=user).order_by('-publication_date')


class IndexDetailView(generic.DetailView):
    model = Question
    template_name = 'polls/polls_detail.html'


class ResultDetailView(generic.DetailView):
    model = Question
    template_name = 'polls/polls_result.html'

@login_required
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

class PollCreateView(LoginRequiredMixin, generic.CreateView):
    model = Question
    fields = ['question_text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def create_choice(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        choice_form = ChoiceFormSet(request.POST, instance=question)
        if choice_form.is_valid():
            choice_form.save()
            messages.success(request, 'New polls have been successfully created!')
            return redirect('polls:polls-index')
    else:
        choice_form = ChoiceFormSet(instance=question)
    context = {'choice_form': choice_form}
    return render(request, 'polls/choice_form.html', context)

@login_required
def update_choice(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        choice_form = ChoiceUpdateFormSet(request.POST, instance=question)
        if choice_form.is_valid():
            choice_form.save()
            messages.success(request, 'Polls have been successfully updated!')
            return redirect('polls:polls-index')
    else:
        choice_form = ChoiceUpdateFormSet(instance=question)
    context = {'choice_form': choice_form, 'question': question}
    return render(request, 'polls/choice_update.html', context)


class PollDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.DeleteView):
    model = Question
    success_url = '/polls/'
    success_message = 'The poll has been deleted!'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False