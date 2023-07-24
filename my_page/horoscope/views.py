from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

zodiac_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


zodiac_date = {
    1: (20, 31, 'capricorn', 'aquarius'),
    2: (19, 29, 'aquarius', 'picses'),
    3: (20, 31, 'picses', 'aries'),
    4: (20, 30, 'aries', 'taurus'),
    5: (21, 31, 'taurus', 'gemini'),
    6: (21, 30, 'gemini', 'cancer'),
    7: (22, 31, 'cancer', 'leo'),
    8: (21, 31, 'leo', 'virgo'),
    9: (22, 30, 'virgo', 'libra'),
    10: (23, 31, 'libra', 'scorpio'),
    11: (22, 30, 'scorpio', 'sagittarius'),
    12: (22, 31, 'sagittarius', 'capricorn'),
}

def index(request):
    zodiacs = list(signs)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse("horoscope-name", args=[sign])
        li_elements += f'<li> <a href="{redirect_path}">{sign.title()}</a> {signs[sign][0]}</li>'
    response = f"""
    <h2>
    <ul>
        {li_elements}
    </ul>
    </h2>
    """
    return HttpResponse(response)


def type_zodiacs(request):
    zodiacs = list(zodiac_element)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse("horoscope-type", args=[sign])
        li_elements += f'<li> <a href="{redirect_path}">{sign.title()}</a></li>'

    response = f"""
        <h2>
        <ul>
            {li_elements}
        </ul>
        </h2>
        """
    return HttpResponse(response)


def get_zodiac_signs_for_elem(request, elements: str):
    li_elements = ''
    for sign in zodiac_element[elements]:
        redirect_path = reverse("horoscope-name", args=[sign])
        li_elements += f'<li> <a href="{redirect_path}">{sign.title()}</a></li>'
    response = f"""
            <h2>
            <ul>
                {li_elements}
            </ul>
            </h2>
            """
    return HttpResponse(response)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    if sign_zodiac.lower() in signs:
        return HttpResponse(f'<h2>{"".join(signs[sign_zodiac.lower()])}</h2>')
    return HttpResponseNotFound(f"Неизвестный знак зодиака {sign_zodiac}")


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(signs)
    if sign_zodiac > len(zodiacs) or sign_zodiac < 1:
        return HttpResponseNotFound(f"Неправильный порядковый номер знака зодиака - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def get_info_about_my_zodiac(request, month: int, day: int, item=None):
    item = zodiac_date.get(month)
    my_zodiac = None
    if day in range(item[0], item[1] + 1):
        my_zodiac = item[3]
    else:
        my_zodiac = item[2]
    redirect_path = reverse("horoscope-name", args=[my_zodiac])
    return HttpResponseRedirect(redirect_path)


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из 4х цифр {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число {sign_zodiac}')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату {sign_zodiac}')
