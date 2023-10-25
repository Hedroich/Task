from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import TaskForm, StatusForm
from .forms import CustomUserCreationForm, CommentForm
from .models import *


@login_required(login_url='index', redirect_field_name=None)
def main(request) -> HttpResponse:
    return render(request, "main.html")


def index(request) -> HttpResponse:
    return render(request, "index.html")


@login_required(login_url='index', redirect_field_name=None)
def all_tasks(request) -> HttpResponse:
    context = {
        "tasks": Task.objects.all(),
    }
    return render(request, "tasks.html", context)


@login_required(login_url='index', redirect_field_name=None)
def add_task(request) -> HttpResponse:
    context = {
        "form": TaskForm(),
        "users": CustomUser.objects.all(),
    }

    if request.method == 'POST':
        task_form = TaskForm(request.POST, request.FILES)
        if task_form.is_valid():
            clean_data = task_form.cleaned_data
            task = Task(
                task_name=clean_data['task_name'],
                description=clean_data['description'],
                status=clean_data['status'],
                completion_date=clean_data['completion_date'],
            )
            task.user_id = request.POST.get("user")
            task.save()
    return render(request, "new_task.html", context)


@login_required(login_url='index', redirect_field_name=None)
def show_task(request, task_id) -> HttpResponse:
    object = Task.objects.get(id=task_id)
    comments = Comment.objects.filter(task=task_id)
    context = {
        "task": object,
        "comments": comments,
        "status_form": StatusForm(),
    }
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        task.status = request.POST.get("update_status")
        task.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    return render(request, "task_view.html", context)


@login_required(login_url='index', redirect_field_name=None)
def add_comment(request,task_id) -> HttpResponse:
    context = {
        "form_comment": CommentForm(),
    }
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        user = CustomUser.objects.get(id=request.user.id)
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            clean_data = comment_form.cleaned_data
            comment = Comment(
                task=task,
                user=user,
                massage=clean_data['massage'],
            )
            comment.save()
        return redirect("task", task_id)
    return render(request, "new_comment.html", context)


def users(request) -> HttpResponse:
    if request.user.is_authenticated:
        return render(request, "main.html")
    else:
        context = {
            "form": CustomUserCreationForm(),
        }
        if request.method == "POST":
            user_form = CustomUserCreationForm(request.POST, request.FILES)
            if user_form.is_valid():
                clean_data = user_form.cleaned_data
                user = CustomUser(
                    name=clean_data['name'],
                    email=clean_data['email'],
                )
                user.set_password(clean_data["password1"])
                user.is_staff = True
                user.is_superuser = True
                user.save()

                return redirect("main")

        return render(request, "users.html", context)
