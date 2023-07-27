from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

# Create your views here.

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


def people_list(request):
    data = {
    'peoples': people
    }
    return render(request, 'blog/people.html', context=data)
def main_page(request):
    # return HttpResponse("Главная страница")
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def posts(request):
    return render(request, 'blog/list_detail.html')


def get_info_about_name_post(request, name_post):
    data = {
        'name': name_post
    }
    if name_post == 'keanu':
        return keanu(request)
    elif name_post == 'records':
        return get_guinness_world_records(request)
    return render(request, 'blog/detail_by_name.html', context=data)


def get_info_about_name_post_by_number(request, number_post: int):
    data = {
        'number': number_post
    }
    return render(request, 'blog/detail_by_number.html', context=data)


def keanu(request):
    data = {
        'year_born': '1964 г.',
        'city_born': 'Бейрут',
        'movie_name': 'На гребне волны',
    }
    return render(request, 'blog/keanu.html', context=data)


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'blog/guinnessworldrecords.html', context=context)
