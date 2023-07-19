from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def monday(request):
    return HttpResponse("Список дел на понедельник")


def tuesday(request):
    return HttpResponse("Список дел на вторник")
