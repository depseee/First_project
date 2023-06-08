from django.urls import path
from . import views

urlpatterns = [
    path('circle/', views.circle),
    path('square/', views.square),
    path('rectangle/', views.rectangle),
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area),
    path('square/<int:side>/', views.get_square_area),
    path('circle/<int:radius>/', views.get_circle_area),
]