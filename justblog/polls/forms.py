from .models import Question, Choice
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']

