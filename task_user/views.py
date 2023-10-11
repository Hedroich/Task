from django.http import HttpResponse
from django.shortcuts import render
from .models import Task, User
from .forms import TaskForm
# Create your views here.


def all_tasks(request):
    context = {
        "tasks": Task.objects.all(),
    }
    return render(request, "tasks.html", context)


def add_task(request):
    context = {
        "form": TaskForm(),
        "users": User.objects.all(),
    }

    if request.method == 'POST':
        task_form = TaskForm(request.POST, request.FILES)
        if task_form.is_valid():
            cd = task_form.cleaned_data
            task = Task(
                task_name=cd['task_name'],
                description=cd['description'],
                completion_date=cd['completion_date'],
            )
            task.user_id = request.POST.get("user")
            task.save()
    return render(request, "new_task.html", context)


def show_task(request, task_id):
    obj = Task.objects.get(id=task_id)
    context = {
        "task": obj
    }
    return render(request, "task_view.html", context)
