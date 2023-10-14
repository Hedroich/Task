from django.contrib import admin
from .models import Task, User, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "password")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_name", "description", "user", "status", "date_of_creation", "completion_date")


@admin.register(Comment)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task", "user", "massage")
