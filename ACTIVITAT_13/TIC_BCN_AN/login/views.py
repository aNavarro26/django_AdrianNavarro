from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import User


# Create your views here.
def home_view(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")

    user = User.objects.get(id=user_id)
    return render(request, "login/home.html", {"user": user})


def login_view(request):
    if request.session.get("user_id"):
        return redirect("home")

    form = LoginForm()
    error_message = ""

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                """
                Sense sessió
                user = User.objects.get(email=email, password=password)
                return render(request, "login/home.html", {"user": user})
                """
                user = User.objects.get(email=email)
                if user.password == password:
                    request.session["user_id"] = user.id
                    return redirect("home")
                else:
                    error_message = "Credencials incorrectes"
            except User.DoesNotExist:
                error_message = "Credencials incorrectes."

    return render(
        request, "login/login.html", {"form": form, "error_message": error_message}
    )


def logout_view(request):
    request.session.flush()
    return redirect("login")
