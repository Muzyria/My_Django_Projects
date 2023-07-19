from django.http import HttpResponse


# Create your views here.


def main_page(request):
    return HttpResponse("Главная страница")


def posts(request):
    return HttpResponse("Все посты блога")

