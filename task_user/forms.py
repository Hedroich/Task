from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("name", "email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("name", "email",)


class TaskForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].queryset = CustomUser.objects.all()

    task_name = forms.CharField(max_length=256, required=True, label="Имя задачи")
    description = forms.CharField(required=True, label="Описание")
    CHOICES_STATUS = (
        ("Pending", "В ожидании"),
        ("In the process.", "В процессе"),
        ("Completed", "Завершено")
    )
    user = forms.ModelMultipleChoiceField(queryset=None, label="Выберите исполнителя")
    status = forms.ChoiceField(choices=CHOICES_STATUS, required=True, label="Статус")
    completion_date = forms.DateTimeField(required=True, label="Дата завершения")


class StatusForm(forms.Form):
    CHOICES_STATUS = (
        ("В процессе", "В процессе"),
        ("Завершено", "Завершено")
    )
    update_status = forms.ChoiceField(choices=CHOICES_STATUS, label="Обновить статус")


class CommentForm(forms.Form):
    massage = forms.CharField(label="Комментарий")



