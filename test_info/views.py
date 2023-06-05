from django.shortcuts import render

# Create your views here.

def keanu(request):
    data = {
        'year_born': '1964 г.',
        'city_born': 'Бейрут, Ливан',
        'movie_name': 'На гребне волны',
    }
    return render(request, 'test_info/info_keanu.html', data)