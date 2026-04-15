from django import forms
from .models import Task

class TaskForm(forms.Form):
    PRIORITY_CHOICES = Task.Priority.choices
    title = forms.CharField(max_length=100)
    description = forms.Textarea()
    due_date = forms.DateField()
    priority = forms.ChoiceField(max_length=100, choices=PRIORITY_CHOICES, default=Task.Priority.MEDIUM)
