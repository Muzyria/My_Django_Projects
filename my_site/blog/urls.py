from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('posts/', views.posts),
    path('posts/<int:number_post>/', views.get_info_about_name_post_by_number),
    path('posts/<str:name_post>/', views.get_info_about_name_post),

]
