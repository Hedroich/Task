from django.shortcuts import render

from .forms import CustomUserCreationForm
from .models import *


# Create your views here.

def users(request):

    context = {
        "form": CustomUserCreationForm(),
    }
    return render(request, "users.html", context)
