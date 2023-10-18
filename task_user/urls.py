from django.urls import path
from .views import all_tasks, add_task, show_task, main, users, index, add_comment

urlpatterns = [
    path('', main, name="main"),
    path('index', index, name="index"),
    path('main/alltask/', all_tasks, name="alltasks"),
    path('main/newtask/', add_task, name="newtask"),
    path('main/showtask/<int:task_id>/', show_task, name="task"),
    path('users/', users, name="users"),
    path('main/showtask/<int:task_id>/newcomment', add_comment, name="newcomment"),
]