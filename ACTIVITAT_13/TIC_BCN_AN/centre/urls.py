from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("students/", views.students, name="students"),
    path("students/<int:student_id>/", views.students, name="student_detail"),
    path("teachers/", views.teachers, name="teachers"),
    path("teachers/<int:teacher_id>/", views.teachers, name="teacher_detail"),
]
