from django.urls import path
from .views import all_tasks, add_task, show_task, main, my_view
from . import views

urlpatterns = [
    path('', main),
    # path('reg/', views.SignUpView.as_view(), name='signup'),
    path('reg/', my_view, name='signup'),
    # path('', index, name="index"),
    path('main/alltask/', all_tasks, name="alltasks"),
    path('main/newtask/', add_task, name="newtask"),
    path('main/showtask/<int:task_id>/', show_task, name="task"),
]