from django.shortcuts import render, redirect
from .forms import TaskForm, StatusForm
from django.shortcuts import render

from .forms import CustomUserCreationForm, CommentForm
from .models import *


def main(request):
    if request.user.is_authenticated:
        return render(request, "main.html")
    else:
        return render(request, "index.html")


def index(request):
    if request.user.is_authenticated:
        return render(request, "main.html")
    else:
        return render(request, "index.html")

def all_tasks(request):
    if request.user.is_authenticated:
        context = {
            "tasks": Task.objects.all(),
        }
        return render(request, "tasks.html", context)
    else:
        return render(request, "index.html")



def add_task(request):

    if request.user.is_authenticated:

        context = {
            "form": TaskForm(),
            "users": CustomUser.objects.all(),
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
    else:
        return render(request, "index.html")


def show_task(request, task_id):
    if request.user.is_authenticated:
        obj = Task.objects.get(id=task_id)
        comments = Comment.objects.filter(task=task_id)
        context = {
            "task": obj,
            "comments": comments,
            "status_form": StatusForm(),
        }
        if request.method == "POST":
            task = Task.objects.get(id=task_id)
            task.status = request.POST.get("update_status")
            task.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        return render(request, "task_view.html", context)
    else:
        return render(request, "index.html")

def add_comment(request,task_id):
    if request.user.is_authenticated:
        context = {
            "form_comment": CommentForm(),

        }
        if request.method == "POST":
            task = Task.objects.get(id=task_id)
            user = CustomUser.objects.get(id=request.user.id)
            comment_form = CommentForm(request.POST, request.FILES)
            if comment_form.is_valid():
                cd = comment_form.cleaned_data
                comment = Comment(
                    task=task,
                    user=user,
                    massage=cd['massage'],
                )
                comment.save()
            return redirect("task", task_id)
        return render(request, "new_comment.html", context)
    else:
        return render(request, "index.html")


def users(request):
    if request.user.is_authenticated:
        return render(request, "main.html")
    else:
        context = {
            "form": CustomUserCreationForm(),
        }
        if request.method == "POST":
            user_form = CustomUserCreationForm(request.POST, request.FILES)
            if user_form.is_valid():
                cd = user_form.cleaned_data
                user = CustomUser(
                    name=cd['name'],
                    email=cd['email'],
                )
                user.set_password("password2")
                user.is_staff = True
                user.is_superuser = True
                user.save()

                return redirect("main")

        return render(request, "users.html", context)
