from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def students(request):
    students = [
        {
            "name": "Roger",
            "surname1": "Sobrino",
            "surname2": "García",
            "email": "roger@example.com",
            "course": "DAW2A",
            "modules": "M07, M08",
        },
        {
            "name": "Oriol",
            "surname1": "Roca",
            "surname2": "Perez",
            "email": "oriol@example.com",
            "course": "DAW2A",
            "modules": "M07, M09",
        },
    ]
    return render(request, "centre/students.html", {"students": students})


def teachers(request):
    teachers = [
        {
            "name": "Josep",
            "surname1": "Roca",
            "surname2": "Martinez",
            "email": "josep@example.com",
            "course": "DAW2A, DAW1A",
            "tutor": True,
            "modules": "M07, M08",
        },
        {
            "name": "Juanma",
            "surname1": "Biel",
            "surname2": "Lopez",
            "email": "juanma@example.com",
            "course": "DAW2B",
            "tutor": False,
            "modules": "M09, M10",
        },
    ]
    return render(request, "centre/teachers.html", {"teachers": teachers})
