from django.db import models


# Create your models here.
class Person(models.Model):
    ROL_CHOICES = [("student", "Student"), ("teacher", "Teacher")]

    rol = models.CharField(
        max_length=10,
        choices=ROL_CHOICES,
        help_text="Rol de la persona: estudiant o professor",
    )
    nom = models.CharField(max_length=50, help_text="Nom de la persona")
    cognom1 = models.CharField(max_length=50, help_text="Primer cognom de la persona")
    cognom2 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Segon cognom de la persona (Opcional)",
    )
    correu = models.EmailField(unique=True, help_text="Correu electrònic de la persona")
    curs = models.CharField(max_length=100, help_text="Cursos associats")
    moduls = models.TextField(help_text="Moduls matriculats o impartits")
    tutor = models.BooleanField(
        default=False, help_text="Es tutor? Només per a professors"
    )

    def __str__(self):
        return f"{self.nom} {self.cognom1} {self.rol}"
