from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def students(request, student_id=None):
    students = [
        {
            "id": 1,
            "nom": "Adrián",
            "cognom1": "Navarro",
            "cognom2": "Perez",
            "correu": "adrian@example.com",
            "curs": "DAW2A",
            "moduls": "M06, M07, M08",
        },
        {
            "id": 2,
            "nom": "Achraf",
            "cognom1": "Chakir",
            "cognom2": "",
            "correu": "achraf@example.com",
            "curs": "DAW2A",
            "moduls": "M06, M07, M09",
        },
        {
            "id": 3,
            "nom": "Xavi",
            "cognom1": "Porras",
            "cognom2": "del Pino",
            "correu": "xavi@example.com",
            "curs": "DAW2A",
            "moduls": "M06, M07, M09",
        },
    ]
    if student_id:
        studentSelected = None
        for student in students:
            if student["id"] == student_id:
                studentSelected = student
                break
        return render(request, "centre/students.html", {"students": studentSelected})

    return render(request, "centre/students.html", {"students": students})


def teachers(request, teacher_id=None):
    teachers = [
        {
            "id": 1,
            "nom": "Roger",
            "cognom1": "Sobrino",
            "cognom2": "Gil",
            "correu": "roger@example.com",
            "rol": "teacher",
            "curs": "DAM2B, DAW2A",
            "tutor": True,
        },
        {
            "id": 2,
            "nom": "Josep Oriol",
            "cognom1": "Roca",
            "cognom2": "Fabra",
            "correu": "josep@example.com",
            "rol": "teacher",
            "curs": "DAW2B, DAW2A, DAW1A",
            "tutor": False,
        },
        {
            "id": 3,
            "nom": "Juanma",
            "cognom1": "Sanchez",
            "cognom2": "Biel",
            "correu": "juanma@example.com",
            "rol": "teacher",
            "curs": "DAW2B, DAW2A",
            "tutor": False,
        },
    ]

    if teacher_id:
        teacherSelected = None
        for teacher in teachers:
            if teacher["id"] == teacher_id:
                teacherSelected = teacher
                break
        return render(request, "centre/teachers.html", {"teachers": teacherSelected})

    return render(request, "centre/teachers.html", {"teachers": teachers})


def index(request):
    students = [
        {"id": 1, "nom": "Adrián", "rol": "student"},
        {"id": 2, "nom": "Achraf", "rol": "student"},
        {"id": 3, "nom": "Xavi", "rol": "student"},
    ]

    teachers = [
        {"id": 1, "nom": "Roger", "rol": "teacher"},
        {"id": 2, "nom": "Josep Oriol", "rol": "teacher"},
        {"id": 3, "nom": "Juanma", "rol": "teacher"},
    ]

    return render(request, "index.html", {"teachers": teachers, "students": students})
