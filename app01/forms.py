from django import forms
from django.forms import widgets as wd

from app01 import models

# class QuestionNaire(forms.Form) :
#     caption = forms.CharField(
#         widget = widgets.Textarea(attrs={"cols":"100", "rows":"2"})
#     )
#     tp = forms.ChoiceField(
#         choices = ((1, '打分(1~10分)'), (2, '单选'), (3, '评价'),),
#         widget = widgets.Select
#     )

class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['caption','tp']


class OptionModelForm(forms.ModelForm):
    class Meta:
        model = models.Option
        fields = ['name','score']