from django.shortcuts import render
from .forms import LoginForm


# Create your views here.
def home(request):
    return render(request, "login/home.html")


def login_view(request):
    form = LoginForm()

    return render(request, "login/login.html", {"form": form})
