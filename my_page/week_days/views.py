from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    return render(request, 'week_days/greeting.html')
    # return HttpResponse(dict_day.get(week_day, f'Не найден день недели {week_day}'))


def get_info_about_week_day_by_number(request, week_day: int):
    if week_day not in range(1, 8):
        return HttpResponseNotFound(f'Неверный номер дня - {week_day}')
    name_days = list(dict_day)[week_day - 1]
    redirect_url = reverse("day_name", args=[name_days])
    return HttpResponseRedirect(redirect_url)
