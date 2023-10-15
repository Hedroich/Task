from django.shortcuts import render, redirect
from .models import Task, User, Comment
from .forms import TaskForm, StatusForm
from django.views.generic import CreateView
from .forms import CreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
# Create your views here.

def main(request):
        return render(request, "main.html")

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
                status=cd['status'],
                completion_date=cd['completion_date'],
            )
            task.user_id = request.POST.get("user")
            task.save()
    return render(request, "new_task.html", context)


def show_task(request, task_id):
    obj = Task.objects.get(id=task_id)
    comments = Comment.objects.filter(task=task_id)
    context = {
        "task": obj,
        "comments": comments,
        "status_form": StatusForm()
    }
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        task.status = request.POST.get("update_status")
        task.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    return render(request, "task_view.html", context)
