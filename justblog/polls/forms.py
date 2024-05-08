from .models import Question, Choice
from django.forms import inlineformset_factory


ChoiceFormSet = inlineformset_factory(Question, Choice, fields=['choice_text'], extra=3, can_delete=False)
ChoiceUpdateFormSet = inlineformset_factory(Question, Choice, fields=['choice_text'], extra=0, can_delete=False)
