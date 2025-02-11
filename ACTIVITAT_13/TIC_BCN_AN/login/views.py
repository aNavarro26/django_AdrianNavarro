from django.shortcuts import render
from .forms import LoginForm
from .models import User


# Create your views here.
def home(request):
    return render(request, "login/home.html")


def login_view(request):
    form = LoginForm()
    error_message = ""

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                user = User.objects.get(email=email, password=password)
                return render(request, "login/home.html", {"user": user})

            except User.DoesNotExist:
                error_message = "Credencials incorrectes."

    return render(
        request, "login/login.html", {"form": form, "error_message": error_message}
    )
