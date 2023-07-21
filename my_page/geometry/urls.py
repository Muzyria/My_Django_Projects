from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:height>/<int:width>', views.get_rectangle_area, name='rectangle'),
    path('square/<int:side>', views.get_square_area, name='square'),
    path('circle/<int:radius>', views.get_circle_area, name='circle'),

    path('get_rectangle_area/<int:height>/<int:width>', views.get_rectangle),
    path('get_square_area/<int:side>', views.get_square),
    path('get_circle_area/<int:radius>', views.get_circle),
]
