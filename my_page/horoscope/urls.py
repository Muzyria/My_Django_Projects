from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")
register_converter(converters.MyFloatConverter, "my_float")
register_converter(converters.MyDateConverter, "my_date")

urlpatterns = [
    path('', views.index),
    path('type/', views.type_zodiacs),

    path('<my_date:sign_zodiac>/', views.get_my_date_converters),

    path('<yyyy:sign_zodiac>/', views.get_yyyy_converters),



    path('type/<elements>/', views.get_zodiac_signs_for_elem, name="horoscope-type"),

    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),

    path('<my_float:sign_zodiac>/', views.get_my_float_converters),

    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),

    path('<int:month>/<int:day>', views. get_info_about_my_zodiac),

]
