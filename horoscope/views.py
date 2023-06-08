from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}


def index(request):
    zodiacs = list(zodiac_dict)
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context)


def info_about_zodiac(request, zodiac: str):
    description = zodiac_dict.get(zodiac, None)
    if description:
        return HttpResponse(f'<h1>{description.split()[0]}<h1/><h2>{description}<h2/>')
    return HttpResponseNotFound('Нет такого знака')


def info_about_zodiac_by_num(request, zodiac: int):
    list_zodiac = list(zodiac_dict)
    if zodiac > len(list_zodiac):
        return HttpResponseNotFound('Нет такого знака зодиака')
    curr_zodiac = list_zodiac[zodiac - 1]
    redirect_url = reverse('zodiac-name', args=(curr_zodiac,))
    return HttpResponseRedirect(redirect_url)


zodiac_elements = {
    'Fire': ['aries', 'leo', 'sagittarius'],
    'Earth': ['taurus', 'virgo', 'capricorn'],
    'Air': ['gemini', 'libra', 'aquarius'],
    'Water': ['cancer', 'scorpio', 'pisces'],
}


def info_about_type(request):
    res_type = ''
    for i in zodiac_elements:
        redirect_path = reverse('element_name', args=[i])
        res_type += f'<li><a href=\'{redirect_path}\'>{i.title()}</a></li>'
    return HttpResponse(f'<ul>{res_type}</ul>')


def info_about_type_zodiac(request, name: str):
    res_el = ''
    for i in zodiac_elements[name]:
        redirect_path = reverse('zodiac-name', args=[i])
        res_el += f"<li><a href='{redirect_path}'>{i.title()}</a></li>"
    return HttpResponse(f'<ul>{res_el}</ul>')
