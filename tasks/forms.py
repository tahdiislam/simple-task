from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "assign_date": forms.DateInput(attrs={"type": "date"}),
            "category": forms.CheckboxSelectMultiple(),
            "description": forms.Textarea(attrs={"rows": 3}),
        }
