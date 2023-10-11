from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Task(models.Model):
    task_name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOICES = (
        ("Pending", "В ожидании"),
        ("In the process.", "В процессе"),
        ("Completed", "Завершено")
    )
    status = models.CharField(max_length=256, choices=CHOICES)
    date_of_creation = models.DateTimeField(auto_created=True, auto_now_add=True)
    completion_date = models.DateTimeField(max_length=256)

    def __str__(self):
        return self.task_name

    def get_absolut_url(self):
        return reverse('task', kwargs={'task_id':self.pk})

