from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def students(request):
    return HttpResponse("Vista alumnes")


def teachers(request):
    return HttpResponse("Vista de professors")
