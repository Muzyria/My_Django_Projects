from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.
def get_rectangle_area(request, height: int, width: int):
    return HttpResponse(f'Площадь прямоугольника размером {height}x{width} равна {height * width}')


def get_square_area(request, side: int):
    return HttpResponse(f'Площадь квадрата размером {side}x{side} равна {side * side}')


def get_circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга радиуса {radius} равна {round(__import__("math").pi * (radius ** 2), 2)}')



def get_rectangle(request, height: int, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{height}/{width}')


def get_square(request, side: int):
    return HttpResponseRedirect(f'/calculate_geometry/square/{side}')


def get_circle(request, radius: int):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')
