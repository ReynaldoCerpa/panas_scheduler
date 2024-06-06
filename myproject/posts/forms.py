from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'datetime-local'}),
        }