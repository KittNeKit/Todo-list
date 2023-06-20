from django import forms

from Task.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline_date", "progres", "tags")


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "name",
