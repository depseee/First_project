from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

dic_week_day = {'monday': 'Понедельник!',
                'tuesday': 'Вторник!',
                'wednesday': 'Среда!',
                'thursday': 'Четверг!',
                'friday': 'Пятница!',
                'saturday': 'Суббота!',
                'sunday': 'Воскресенье!', }


def get_info_about_day(request, day):
    description = dic_week_day.get(day, None)
    if description:
        return HttpResponse(f'{description}')
    return HttpResponseNotFound(f'Нет такого дня недели: {description}')


def get_info_about_day_by_num(request, day: int):
    days = list(dic_week_day)
    if day > len(days):
        return HttpResponseNotFound(f'Нет дня с такой цифрой')
    res_day = days[day - 1]
    redirect_url = reverse('week_days-name', args=(res_day,))
    return HttpResponseRedirect(redirect_url)
