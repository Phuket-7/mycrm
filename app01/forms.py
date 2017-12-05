from django import forms
from django.forms import widgets

class QuestionNaire(forms.Form) :
    caption = forms.CharField(
        widget = widgets.Textarea(attrs={"cols":"100", "rows":"2"})
    )
    tp = forms.ChoiceField(
        choices = ((1, '打分(1~10分)'), (2, '单选'), (3, '评价'),),
        widget = widgets.Select
    )