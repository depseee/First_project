from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template.loader import render_to_string


# Create your views here.


def get_rectangle_area(request, width: int, height: int):
    area = width * height
    return HttpResponse(f'Площадь прямоугольника {width} на {height} равна {area}')


def get_square_area(request, side: int):
    area = side ** 2
    return HttpResponse(f'Площадь квадрата со стороной {side} равна {area}')


def get_circle_area(request, radius: int):
    area = 3.14 * radius ** 2
    return HttpResponse(f'Площадь круга с радиусом {radius} равна {area}')


def circle(request):
    response = render_to_string('geometry/circle.html')
    return HttpResponse(response)


def square(request):
    response = render_to_string('geometry/square.html')
    return HttpResponse(response)


def rectangle(request):
    response = render_to_string('geometry/rectangle.html')
    return HttpResponse(response)