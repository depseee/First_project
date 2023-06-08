from django.shortcuts import render


# Create your views here.

def keanu(request):
    data = {
        'year_born': '1964 г.',
        'city_born': 'Бейрут, Ливан',
        'movie_name': 'На гребне волны',
    }
    return render(request, 'info/info_keanu.html', data)


def power_man(request):
    data = {'power_man': 'Narve Laeret'}
    return render(request, 'info/guinnessworldrecords1.html', data)


def bar_name(request):
    data = {'bar_name': 'Bob’s BBQ & Grill'}
    return render(request, 'info/guinnessworldrecords2.html', data)


def count_needle(request):
    data = {'count_needle': 1790}
    return render(request, 'info/guinnessworldrecords3.html', data)


people = [
    {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
    {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
    {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
    {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
    {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
    {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
    {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
    {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
    {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
    {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
]


def people_info(request):
    context = {
        'people': people,
    }
    return render(request, 'info/people.html', context)


def table(request):
    return render(request, 'info/table.html')