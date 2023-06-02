from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('type/', views.info_about_type),
    path('type/<str:name>/', views.info_about_type_zodiac, name='element_name'),

    path('<int:zodiac>/', views.info_about_zodiac_by_num),
    path('<str:zodiac>/', views.info_about_zodiac, name='zodiac-name'),
]