from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.name

    def __str__(self):
        return self.email


class Task(models.Model):
    task_name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
        return reverse('task', kwargs={'task_id': self.pk})


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    massage = models.TextField(blank=True)

