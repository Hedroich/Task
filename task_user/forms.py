from django import forms
from .models import Task, User
from django.forms import ModelChoiceField


class TaskForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].queryset = User.objects.all()

    task_name = forms.CharField(max_length=256, required=False)
    description = forms.CharField(required=False)
    # CHOICES_STATUS = (
    #     ("Pending", "В ожидании"),
    #     ("In the process.", "В процессе"),
    #     ("Completed", "Завершено")
    # )
    user = forms.ModelMultipleChoiceField(queryset=None)
    # status = forms.ChoiceField(choices=CHOICES_STATUS, required=False)
    completion_date = forms.DateTimeField(required=False)


