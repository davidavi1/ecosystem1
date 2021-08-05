from django import forms
from .models import FeedBackModel


class FeedBackForms(forms.ModelForm):
    class Meta:
        model = FeedBackModel
        fields = ('name', 'last_name', 'subject', 'text')
