from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass

# Create your views here.
signs = {
    'aries': ["♈", "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)."],
    'taurus': ["♉", "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)."],
    'gemini': ["♊", "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)."],
    'cancer': ["♋", "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)."],
    'leo': ["♌", "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)."],
    'virgo': ["♍", "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)."],
    'libra': ["♎", "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)."],
    'scorpio': ["♏", "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)."],
    'sagittarius': ["♐", "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)."],
    'capricorn': ["♑", "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)."],
    'aquarius': ["♒", "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)."],
    'pisces': ["♓", "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."]
}


def index(request):
    zodiacs = list(signs)
    context = {
        "zodiacs": zodiacs,
        "zodiac_dict": signs
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = " ".join(signs.get(sign_zodiac))
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac.title(),

    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(signs)
    if sign_zodiac > len(zodiacs) or sign_zodiac < 1:
        return HttpResponseNotFound(f"Неправильный порядковый номер знака зодиака - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)
