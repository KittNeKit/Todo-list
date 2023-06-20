from django import forms

from Task.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline_date = forms.DateTimeField(
         widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
         required=False
     )

    class Meta:
        model = Task
        fields = ("content", "deadline_date", "progres", "tags")


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "name",
