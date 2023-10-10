from django.urls import path
from .views import all_tasks, add_task

urlpatterns = [
    path('', all_tasks),
    path('newtask', add_task, name="newtask")
]