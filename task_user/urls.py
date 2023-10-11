from django.urls import path
from .views import all_tasks, add_task, show_task

urlpatterns = [
    path('', all_tasks),
    path('newtask/', add_task, name="newtask"),
    path('showtask/<int:task_id>/', show_task, name="task")
]