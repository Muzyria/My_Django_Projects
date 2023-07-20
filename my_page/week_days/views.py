from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
dict_day = {
    'monday': 'Пн - стирать',
    'tuesday': 'Вт - учиться',
    'wednesday': 'Ср - гладить',
    'thursday': 'Чт - футбол',
    'friday': 'Пт - кино',
    'saturday': 'Сб - вино',
    'sunday': 'Вс - лежать',
}


def get_info_about_week_day(request, week_day: str):
    return HttpResponse(dict_day.get(week_day, f'Не найден день недели {week_day}'))


def get_info_about_week_day_by_number(request, week_day: int):
    if week_day not in range(1, 8):
        return HttpResponseNotFound(f'Неверный номер дня - {week_day}')
    name_days = list(dict_day)
    return HttpResponseRedirect(f'/todo_week/{name_days[week_day - 1]}')
