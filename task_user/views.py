from django.shortcuts import render, redirect
from .models import Task, User, Comment
from .forms import TaskForm, StatusForm
from django.views.generic import CreateView
from .forms import CreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
# Create your views here.


class SignUpView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("signup")
    template_name = "signup.html"


def my_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "main.html")
    else:
        return render(request, "signup.html")
    #     ...
    # else:
    #     # Return an 'invalid login' error message.


def main(request):
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
        return render(request, "signup.html")


def add_task(request):
    if request.user.is_authenticated:
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
    else:
        return render(request, "signup.html")


def show_task(request, task_id):
    if request.user.is_authenticated:
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
    else:
        return render(request, "signup.html")