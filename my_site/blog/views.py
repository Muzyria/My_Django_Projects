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
    return HttpResponse(f"Информация о посте {name_post}")


def get_info_about_name_post_by_number(request, number_post: int):
    return HttpResponse(f"Здесь содержится информация о посте под номером {number_post}")
