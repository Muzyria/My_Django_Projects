from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.type_zodiacs),
    path('type/<elements>/', views.get_zodiac_signs_for_elem, name="horoscope-type"),
    # path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
]
