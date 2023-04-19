from django import forms


class AnswerForm(forms.Form):
    prompt = forms.CharField(max_length=150)