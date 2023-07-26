from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

# Create your views here.


def main_page(request):
    # return HttpResponse("Главная страница")
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def posts(request):
    return render(request, 'blog/list_detail.html')


def get_info_about_name_post(request, name_post):
    if name_post == 'keanu':
        return keanu(request)
    elif name_post == 'records':
        return get_guinness_world_records(request)
    return HttpResponse(f"Информация о посте {name_post}")


def get_info_about_name_post_by_number(request, number_post: int):
    return HttpResponse(f"Здесь содержится информация о посте под номером {number_post}")


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
