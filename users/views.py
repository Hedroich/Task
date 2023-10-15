from django.shortcuts import render
from .models import *


# Create your views here.

def users(request):
    users = CustomUserManager.objects.all()
    context = {
        users,
    }
    return render(request, "users.html", context)
