from django import forms
from .models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {
            "password": forms.PasswordInput(attrs={"placeholder": "Contrasenya"})
        }
