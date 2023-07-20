from django.http import HttpResponse


# Create your views here.


def main_page(request):
    return HttpResponse("Главная страница")


def posts(request):
    return HttpResponse("Все посты блога")


def get_info_about_name_post(request, name_post):
    return HttpResponse(f"Информация о посте {name_post}")
